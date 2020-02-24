from django.urls import path
from . import views

app_name = 'shadownetz'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('newsletter/signup', views.newsletter, name='newslettersignup'),
    path('status/email-origin', views.does_email_exist, name="emailOriginStatus")
]
