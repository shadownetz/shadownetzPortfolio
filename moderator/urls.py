from django.urls import path
from . import views

app_name = "shadownetz_moderator"

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name="authentication"),
    path('auth/login', views.auth_login, name="authenticateLogin"),
    path('auth/logout', views.logout_user, name="logoutUser")
]
