from django.shortcuts import render
from .app_functions import DevelopersHubBlogClass
from django.http import JsonResponse

developers_hub_init = DevelopersHubBlogClass()


def index(request):
    context = {
        "ready": True
    }
    page = request.GET.get('page')
    context['blogs'] = developers_hub_init.get_blog_content(page, 5)
    return render(request, 'developershub/index.html', context)


def display_blog(request):
    post_id = request.GET.get('post-id')
    comments = developers_hub_init.get_comments(post_id)
    context = {
        'blog': developers_hub_init.get_single_blog_content(post_id),
        'previous_blog': developers_hub_init.get_previous_single_blog_content(post_id),
        'next_blog': developers_hub_init.get_next_single_blog_content(post_id),
        'comments': comments[0],
        'number_of_comments': comments[1]
    }
    return render(request, 'developershub/single-blog.html', context)


def post_comment(request):
    data = {'post_status': False}
    if request.method == 'POST':
        blog_id = request.POST['id']
        user_email = request.POST['email']
        message = request.POST['message']
        if user_email and message:
            post_status = developers_hub_init.post_comment(blog_id, user_email, message)
            if post_status:
                data['post_status'] = True
    return JsonResponse(data=data)
