from django import forms
from .models import (NewsLetterSubscription, Contact)


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSubscription
        exclude = ['dateCreated']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['dateCreated']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Message'
            }),
        }