from django.db import models
from django.conf import settings


class SocialLifeBlog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    tags = models.CharField(max_length=500, blank=True, null=True)
    views = models.IntegerField(default=0)
    display_image = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + '_' + str(self.id) + '_blog'


class SocialLifeBlogComment(models.Model):
    user = models.EmailField(blank=False)
    blog = models.ForeignKey(settings.SOCIAL_LIFE_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)