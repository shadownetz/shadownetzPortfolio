from django.shortcuts import render, redirect, reverse
from .models import (User, NewsLetterSubscription)
from .forms import NewsletterForm, ContactForm
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.conf import settings


def index(request):
    newsletterform = NewsletterForm()
    context = {
        'newsletterform': newsletterform
    }

    return render(request, 'home/index.html', context)


def propush_js(request):
    with open(settings.PROPUSH_URL+'/sw-07c23.js', 'r') as file:
        file_content = file.read()
    return HttpResponse(file_content, content_type="text/javascript")


class ContactView(View):
    contact_form = ContactForm()

    def get(self, request):
        context = {
            'contactForm': self.contact_form
        }
        try:
            tmp = request.session.get('contact_saved')
            if tmp:
                context['contact_is_submitted'] = True
                del request.session['contact_saved']
        except KeyError:
            pass
        return render(request, 'home/contact.html', context)

    def post(self, request):
        new_contact = ContactForm(request.POST)
        if new_contact.is_valid():
            new_contact.save()
            request.session['contact_saved'] = True
            return redirect(reverse('shadownetz:contact'))
        self.context['contactForm'] = ContactForm()


def newsletter(request):
    save_status = False
    email_exist_status = True
    if request.method == 'POST':
        news_letter_field = NewsletterForm(request.POST)
        if news_letter_field.is_valid():
            email_value = news_letter_field.cleaned_data['email']
            if not NewsLetterSubscription.objects.filter(email=email_value).exists():
                news_letter_field.save()
                save_status = True
                email_exist_status = False
    return JsonResponse(data={
        'is_saved': save_status,
        'email_exists': email_exist_status
    })


def does_email_exist(request):
    email = request.GET.get('email')
    return_data = {'exist': User.objects.filter(email=email).exists()}
    return JsonResponse(data=return_data)
