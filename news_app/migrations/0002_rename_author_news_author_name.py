# Generated by Django 4.2 on 2025-04-10 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='author',
            new_name='author_name',
        ),
    ]
