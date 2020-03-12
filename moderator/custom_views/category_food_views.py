from django.shortcuts import render, redirect, reverse
from ..scripts.forms.categories.food import forms as foodforms
from food.models import FoodBlog
from ..scripts.utils.mainUtil import *


def view_food_category(request):
    context = {}
    return render(request, 'moderator/categories/food/dashboard.html', context)


def new_food_content(request):
    context = {
        "custom_images": get_custom_blog_pictures('developershub')
    }
    new_content_form = foodforms.NewContentForm()
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

    return render(request, 'moderator/categories/food/newcontent.html', context)


def process_food_content(request):
    if request.method == 'POST':
        blog_title = request.POST["title"]
        blog_content = request.POST["content"]
        blog_tags = request.POST["tags"]
        blog_display_image = request.POST["display_image"]
        if blog_title and blog_content and blog_display_image:
            blog_object = FoodBlog.objects.create(
                user=request.user, title=blog_title, content=blog_content,
                tags=blog_tags, display_image=blog_display_image
            )
            if blog_object:
                request.session["new_blog_save_status"] = True
            else:
                request.session["new_blog_save_status"] = False
    return redirect(reverse('shadownetz_moderator:category_food_add'))
