from django.shortcuts import render
from .app_functions import BlogClass

blog_init = BlogClass()


def index(request):
    context = {
        'ready': True
    }
    page = request.GET.get('page')
    query = request.GET.get('q')
    if query:
        context['blogs'] = blog_init.fetch_blog_items(page, 5, query)
    else:
        context['blogs'] = blog_init.fetch_blog_items(page, 5)
    context['popular_post_developer_hub'] = blog_init.fetch_popular_post_developers_hub()
    context['popular_post_food'] = blog_init.fetch_popular_post_food()
    context['popular_post_movies'] = blog_init.fetch_popular_post_movies()
    context['popular_post_social_life'] = blog_init.fetch_popular_post_social_life()
    context['popular_post_trending'] = blog_init.fetch_popular_post_trending()
    context['popular_post_sport'] = blog_init.fetch_popular_post_sport()

    context['count_dev_hub_post'] = blog_init.fetch_number_developer_hub_post()
    context['count_food_post'] = blog_init.fetch_number_food_post()
    context['count_movies_post'] = blog_init.fetch_number_movies_post()
    context['count_social_life_post'] = blog_init.fetch_number_social_life_post()
    context['count_trending_post'] = blog_init.fetch_number_trending_post()
    context['count_sport_post'] = blog_init.fetch_number_sport_post()

    return render(request, 'blog/index.html', context)
