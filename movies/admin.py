from django.contrib import admin
from .models import *


class MovieBlogAdmin(admin.ModelAdmin):
    model = MovieBlog
    list_display = (
        'id', 'user', 'author', 'title', 'content', 'tags', 'views', 'comments', 'url', 'display_image',
        'date_created'
    )
    list_filter = ('user', 'date_created')
    fieldsets = (
        (None, {'fields': (
            'user', 'author', 'title', 'content', 'tags', 'views', 'comments', 'url', 'display_image',
        )}),
    )
    search_fields = ('user',)
    ordering = ('date_created',)


class MovieBlogCommentAdmin(admin.ModelAdmin):
    model = MovieBlogComment
    list_display = (
        'id', 'user', 'blog', 'message', 'date_created'
    )
    list_filter = ('user', 'date_created')
    fieldsets = (
        (None, {'fields': (
            'user', 'blog', 'message',
        )}),
    )
    search_fields = ('user',)
    ordering = ('date_created',)


admin.site.register(MovieBlog, MovieBlogAdmin)
admin.site.register(MovieBlogComment, MovieBlogCommentAdmin)
