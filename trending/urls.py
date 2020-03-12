from django.urls import path
from . import views

app_name = "shadownetz_trendingblog"

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.display_blog, name="display_blog"),
    path('blog/post/comment', views.post_comment, name="post_comment"),
    path('blog/get/new-comment', views.fetch_latest_comment, name="fetch_new_comments")
]
