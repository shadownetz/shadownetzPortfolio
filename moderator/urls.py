from django.urls import path
from . import views
from .custom_views import (category_developershub_views, category_socialife_views,
                           category_food_views, category_sport_views,
                           category_movies_views, category_trending_views)

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
    path('categories/developershub/new/template/', category_developershub_views.new_developers_hub_content_from_template,
         name="category_developershub_add_template"),
    path('categories/developershub/new/template/process', category_developershub_views.process_new_developers_hub_content_from_template,
         name="process_category_developershub_add_template"),

    # Social Life Category
    path('categories/social-life', category_socialife_views.view_social_life_category,
         name="category_sociallife"),
    path('categories/social-life/new', category_socialife_views.new_social_life_content, name="category_sociallife_add"),
    path('categories/social-life/new/process', category_socialife_views.process_social_life_content,
         name="process_category_sociallife_add"),
    path('categories/social-life/new/template', category_socialife_views.new_social_life_content_from_template,
         name="category_sociallife_add_template"),
    path('categories/social-life/new/template/process', category_socialife_views.process_social_life_content_from_template,
         name="process_category_sociallife_add_template"),

    # Food Category
    path('categories/food', category_food_views.view_food_category, name="category_food"),
    path('categories/food/new', category_food_views.new_food_content, name="category_food_add"),
    path('categories/food/new/process', category_food_views.process_food_content,
         name="process_category_food_add"),
    path('categories/food/new/template', category_food_views.new_food_content_from_template, name="category_food_add_template"),
    path('categories/food/new/template/process', category_food_views.process_food_content_from_template,
         name="process_category_food_add_template"),

    # Sport Category
    path('categories/sport', category_sport_views.view_sport_category, name="category_sport"),
    path('categories/sport/new', category_sport_views.new_sport_content, name="category_sport_add"),
    path('categories/sport/new/process', category_sport_views.process_sport_content,
         name="process_category_sport_add"),
    path('categories/sport/new/template', category_sport_views.new_sport_content_from_template, name="category_sport_add_template"),
    path('categories/sport/new/template/process', category_sport_views.process_sport_content_from_template,
         name="process_category_sport_add_template"),

    # Movies Category
    path('categories/movies', category_movies_views.view_movies_category, name="category_movies"),
    path('categories/movies/new', category_movies_views.new_movies_content, name="category_movies_add"),
    path('categories/movies/new/process', category_movies_views.process_new_movies_content,
         name="process_category_movies_add"),
    path('categories/movies/new/template', category_movies_views.new_developers_hub_content_from_template, name="category_movies_add_template"),
    path('categories/movies/new/template/process', category_movies_views.process_new_developers_hub_content_from_template,
         name="process_category_movies_add_template"),

    # Trending Category
    path('categories/trending', category_trending_views.view_trending_category, name="category_trending"),
    path('categories/trending/new', category_trending_views.new_trending_content, name="category_trending_add"),
    path('categories/trending/new/process', category_trending_views.process_trending_content,
         name="process_category_trending_add"),


]
