from django.shortcuts import render, redirect, reverse
from .models import (User, NewsLetterSubscription)
from .forms import NewsletterForm, ContactForm
from django.http import JsonResponse


def index(request):
    newsletterform = NewsletterForm()
    context = {
        'newsletterform': newsletterform
    }

    return render(request, 'home/index.html', context)


def contact(request):
    contact_form = ContactForm()
    context = {
        'contactForm': contact_form,
        'contact_submitted': False
    }
    try:
        request.session.get('contact_saved')
        context['contact_submitted'] = True
        del request.session['contact_saved']
    except KeyError:
        pass

    if request.method == 'POST':
        new_contact = ContactForm(request.POST)
        if new_contact.is_valid():
            new_contact.save()
            request.session['contact_saved'] = True
            return redirect(reverse('shadownetz:contact'))
    return render(request, 'home/contact.html', context)


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
