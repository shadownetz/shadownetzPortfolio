from django.contrib import admin
from .models import *


class FoodBlogAdmin(admin.ModelAdmin):
    model = FoodBlog
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


class FoodBlogCommentAdmin(admin.ModelAdmin):
    model = FoodBlogComment
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


admin.site.register(FoodBlog, FoodBlogAdmin)
admin.site.register(FoodBlogComment, FoodBlogCommentAdmin)
