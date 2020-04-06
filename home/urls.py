from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shadownetz'

urlpatterns = [
    path('', views.index, name="index"),
    # ProPush JS Verification
    path('sw-07c23.js', views.propush_js, name="propush-js"),

    path('contact', views.ContactView.as_view(), name="contact"),
    path('newsletter/signup', views.newsletter, name='newslettersignup'),
    path('status/email-origin', views.does_email_exist, name="emailOriginStatus")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
