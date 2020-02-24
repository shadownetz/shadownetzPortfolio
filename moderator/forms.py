from django import forms
from home.models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-center',
        'placeholder': "Email Address"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Password'
    }))
