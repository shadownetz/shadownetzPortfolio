from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import user_passes_test
from django.conf import settings
from .forms import *


@user_passes_test(lambda x: True if x.is_staff and x.is_superuser else False,
                  login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'moderator/index.html', {})


def auth(request):
    login_form = LoginForm()
    context = {
        'loginForm': login_form
    }

    # failed login attempt
    try:
        context['loginErrorMessage'] = request.session['loginErrorMessage']
        del request.session['loginErrorMessage']
    except KeyError:
        pass

    return render(request, 'moderator/login.html', context)


def auth_login(request):
    auth_redirect = reverse('shadownetz_moderator:authentication')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        nextURL = request.POST['next']
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user=user)
                if len(nextURL) > 0:
                    return redirect(nextURL)
                return redirect(reverse('shadownetz_moderator:index'))
            else:
                request.session['loginErrorMessage'] = "Invalid Login Credentials"
        if len(nextURL) > 0:
            auth_redirect += "?next={}".format(nextURL)
    return redirect(auth_redirect)


def logout_user(request):
    logout(request)
    return redirect(reverse('shadownetz_moderator:authentication'))
