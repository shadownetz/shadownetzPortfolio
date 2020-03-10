from django.urls import path
from . import views
from .custom_views import category_developershub_views

app_name = "shadownetz_moderator"

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name="authentication"),
    path('auth/login', views.auth_login, name="authenticateLogin"),
    path('auth/logout', views.logout_user, name="logoutUser"),
    path('categories/developershub', category_developershub_views.view_developers_hub_category, name="category_developershub"),
    path('categories/developershub/new', category_developershub_views.new_developers_hub_content, name="category_developershub_add"),
    path('categories/developershub/new/process', category_developershub_views.process_new_developers_hub_content,
         name="process_category_developershub_add"),

]
