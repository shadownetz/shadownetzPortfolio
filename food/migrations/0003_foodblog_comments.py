# Generated by Django 3.0 on 2020-03-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20200312_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodblog',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]