from django.shortcuts import render
from .app_functions import DevelopersHubBlogClass
from django.http import JsonResponse

developers_hub_init = DevelopersHubBlogClass()


def index(request):
    context = {
        "ready": True
    }
    page = request.GET.get('page')
    query = request.GET.get('q')
    if query:
        context['blogs'] = developers_hub_init.filter_blog_content_by_search(query, page, 5)
    else:
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


def fetch_latest_comment(request):
    if request.method == 'GET':
        data = {"new_comments": [], "new_no_of_comment": 0}
        index_of_last_comment = request.GET.get('last_comment_index')
        blog_id = request.GET.get('blog_id')

        try:
            index_of_last_comment = int(index_of_last_comment)
        except TypeError:
            index_of_last_comment = 0

        new_comment_objects = developers_hub_init.get_comment_greater_than_id(blog_id, index_of_last_comment)
        if new_comment_objects:
            for obj in new_comment_objects:
                tmp_obj = {'id': obj.id, 'user': obj.user, 'date_created': obj.date_created, 'message': obj.message}
                data["new_comments"].append(tmp_obj)
                data["new_no_of_comment"] = developers_hub_init.get_total_no_of_comment(blog_id)
        # data["new_comments"] = new_comment_objects[0] if new_comment_objects[0] else []
        return JsonResponse(data=data)
