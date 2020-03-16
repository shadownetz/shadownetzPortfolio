# Generated by Django 3.0 on 2020-03-16 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trending', '0002_trendingblog_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendingblog',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='trendingblog',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='trendingblog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
