# Generated by Django 3.0 on 2020-03-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developershub', '0004_developershubblog_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='developershubblog',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
