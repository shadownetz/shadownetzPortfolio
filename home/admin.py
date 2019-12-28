from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, NewsLetterSubscription, Contact


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'password', 'is_superuser',
        'is_active', 'avatar', 'date_created', 'last_login'
    )
    list_filter = ('email', 'is_active', 'date_created', 'last_login')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'password', 'email')}),
        ('Avatar', {'fields': ('avatar',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('avatar', 'first_name', 'last_name', 'password', 'email',)
                }),
        ('Permissions', {'fields': ('is_active',)})
    )
    search_fields = ('email',)
    ordering = ('date_created',)


class NewsletterAdmin(admin.ModelAdmin):
    model = NewsLetterSubscription
    list_display = ('email', 'dateCreated')
    fieldsets = (
        (None, {'fields': ('email',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'dateCreated')}),
    )
    ordering = ('dateCreated',)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'subject', 'message', 'dateCreated')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'subject', 'message')}),
    )
    add_fieldsets = (
        (None, {'fields': ('name', 'email', 'subject', 'message', 'dateCreated')}),
    )
    ordering = ('dateCreated', 'email')


admin.site.register(User, CustomUserAdmin)
admin.site.register(NewsLetterSubscription, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
