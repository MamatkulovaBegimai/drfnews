# Generated by Django 4.2 on 2025-04-11 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author_name',
        ),
    ]
