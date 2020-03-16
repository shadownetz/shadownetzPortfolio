from django.contrib import admin
from .models import *


class DevelopersHubBlogAdmin(admin.ModelAdmin):
    model = DevelopersHubBlog
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


class DevelopersHubBlogCommentAdmin(admin.ModelAdmin):
    model = DevelopersHubBlogComment
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


admin.site.register(DevelopersHubBlog, DevelopersHubBlogAdmin)
admin.site.register(DevelopersHubBlogComment, DevelopersHubBlogCommentAdmin)
