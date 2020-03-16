from django.shortcuts import render, redirect, reverse
from ..scripts.forms.categories.movies import forms as moviesforms
from movies.models import MovieBlog
from ..scripts.utils.mainUtil import *
from ..scripts.utils.blogContent import BlogContentTemplate
import datetime

blog_content_init = BlogContentTemplate()


def view_movies_category(request):
    context = {}
    return render(request, 'moderator/categories/movies/dashboard.html', context)


def new_movies_content(request):
    context = {
        "custom_images": get_custom_blog_pictures('developershub')
    }
    new_content_form = moviesforms.NewContentForm()
    context["new_content_form"] = new_content_form
    # new blog save status
    try:
        save_status = request.session["new_blog_save_status"]
        if save_status is True:
            context["add_content_save_status"] = True
        else:
            context["add_content_save_status"] = False
        del request.session["new_blog_save_status"]
    except KeyError:
        pass

    return render(request, 'moderator/categories/movies/newcontent.html', context)


def process_new_movies_content(request):
    if request.method == 'POST':
        blog_title = request.POST["title"]
        blog_content = request.POST["content"]
        blog_tags = request.POST["tags"]
        blog_display_image = request.POST["display_image"]
        if blog_title and blog_content and blog_display_image:
            blog_object = MovieBlog.objects.create(
                user=request.user, title=blog_title, content=blog_content,
                tags=blog_tags, display_image=blog_display_image
            )
            if blog_object:
                request.session["new_blog_save_status"] = True
            else:
                request.session["new_blog_save_status"] = False
    return redirect(reverse('shadownetz_moderator:category_movies_add'))


def new_developers_hub_content_from_template(request):
    context = {'blogs': None}
    page = request.GET.get('page')

    try:
        page = int(page)
    except TypeError:
        page = 1


    # new blog save status
    try:
        save_status = request.session["new_blog_save_status"]
        if save_status is True:
            context["add_content_save_status"] = True
        else:
            context["add_content_save_status"] = False
        del request.session["new_blog_save_status"]
    except KeyError:
        pass

    if page:
        context['blogs'] = blog_content_init.get_content(context="movies", tag="movies, leisure", page=page)
    else:
        context['blogs'] = blog_content_init.get_content(context="programming", tag="movies, leisure")

    return render(request, 'moderator/categories/movies/new_content_template.html', context=context)


def process_new_developers_hub_content_from_template(request):
    if request.method == 'POST':
        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        post_tags = request.POST['post_tags']
        post_image = request.POST['post_image']
        post_date = request.POST['post_date']
        post_user = request.POST['post_user']
        post_url = request.POST['post_url']
        if post_date:
            post_date = post_date.replace('T', ' ')
            post_date = datetime.datetime.strptime(post_date, '%Y-%m-%d %H:%M:%S%z')

        blog_object = MovieBlog.objects.create(
            author=post_user, title=post_title, content=post_content, url=post_url,
            tags=post_tags, display_image=post_image, date_created=post_date
        )
        if blog_object:
            request.session["new_blog_save_status"] = True
        else:
            request.session["new_blog_save_status"] = False
    return redirect(reverse('shadownetz_moderator:category_movies_add_template'))
