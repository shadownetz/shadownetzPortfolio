from django.contrib import admin
from .models import *


class SocialLifeBlogAdmin(admin.ModelAdmin):
    model = SocialLifeBlog
    list_display = (
        'id', 'user', 'title', 'content', 'tags', 'views', 'comments', 'display_image',
        'date_created'
    )
    list_filter = ('user', 'date_created')
    fieldsets = (
        (None, {'fields': (
            'user', 'title', 'content', 'tags', 'views', 'comments', 'display_image',
        )}),
    )
    search_fields = ('user',)
    ordering = ('date_created',)


class SocialLifeBlogCommentAdmin(admin.ModelAdmin):
    model = SocialLifeBlogComment
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


admin.site.register(SocialLifeBlog, SocialLifeBlogAdmin)
admin.site.register(SocialLifeBlogComment, SocialLifeBlogCommentAdmin)
