from django.urls import path
from . import views

app_name = 'shadownetz'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('newsletter/signup', views.newsletter, name='newslettersignup')
]
