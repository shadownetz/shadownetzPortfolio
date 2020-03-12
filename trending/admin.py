from django.contrib import admin
from .models import *


class TrendingBlogAdmin(admin.ModelAdmin):
    model = TrendingBlog
    list_display = (
        'id', 'user', 'title', 'content', 'tags', 'views', 'display_image',
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


class TrendingBlogCommentAdmin(admin.ModelAdmin):
    model = TrendingBlogComment
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


admin.site.register(TrendingBlog, TrendingBlogAdmin)
admin.site.register(TrendingBlogComment, TrendingBlogCommentAdmin)
