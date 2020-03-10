from django.shortcuts import render, redirect, reverse
from ..scripts.forms.categories.developershub import forms as developershubforms
from developershub.models import DevelopersHubBlog
from ..scripts.utils.mainUtil import *


def view_developers_hub_category(request):
    context = {}
    return render(request, 'moderator/categories/developershub/dashboard.html', context)


def new_developers_hub_content(request):
    context = {
        "custom_images": get_custom_blog_pictures('developershub')
    }
    new_content_form = developershubforms.NewContentForm()
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

    return render(request, 'moderator/categories/developershub/newcontent.html', context)


def process_new_developers_hub_content(request):
    if request.method == 'POST':
        blog_title = request.POST["title"]
        blog_content = request.POST["content"]
        blog_tags = request.POST["tags"]
        blog_display_image = request.POST["display_image"]
        if blog_title and blog_content and blog_display_image:
            blog_object = DevelopersHubBlog.objects.create(
                user=request.user, title=blog_title, content=blog_content,
                tags=blog_tags, display_image=blog_display_image
            )
            if blog_object:
                request.session["new_blog_save_status"] = True
            else:
                request.session["new_blog_save_status"] = False
    return redirect(reverse('shadownetz_moderator:category_developershub_add'))
