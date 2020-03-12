from django.contrib import admin
from .models import *


class SportBlogAdmin(admin.ModelAdmin):
    model = SportBlog
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


class SportBlogCommentAdmin(admin.ModelAdmin):
    model = SportBlogComment
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


admin.site.register(SportBlog, SportBlogAdmin)
admin.site.register(SportBlogComment, SportBlogCommentAdmin)
