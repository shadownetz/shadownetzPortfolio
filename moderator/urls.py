from django.urls import path
from . import views
from .custom_views import category_developershub_views, category_socialife_views

app_name = "shadownetz_moderator"

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name="authentication"),
    path('auth/login', views.auth_login, name="authenticateLogin"),
    path('auth/logout', views.logout_user, name="logoutUser"),
    # Developers Hub Category
    path('categories/developershub', category_developershub_views.view_developers_hub_category, name="category_developershub"),
    path('categories/developershub/new', category_developershub_views.new_developers_hub_content, name="category_developershub_add"),
    path('categories/developershub/new/process', category_developershub_views.process_new_developers_hub_content,
         name="process_category_developershub_add"),
    # Social Life Category
    path('categories/social-life', category_socialife_views.view_social_life_category,
         name="category_sociallife"),
    path('categories/social-life/new', category_socialife_views.new_social_life_content, name="category_sociallife_add"),
    path('categories/social-life/new/process', category_socialife_views.process_social_life_content,
         name="process_category_sociallife_add"),


]
