# Generated by Django 3.0 on 2019-12-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_newslettersubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='contact name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('subject', models.CharField(max_length=100, verbose_name='contact subject')),
                ('message', models.TextField(max_length=200, verbose_name='contact message')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
