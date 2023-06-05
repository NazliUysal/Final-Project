# Generated by Django 4.2.1 on 2023-06-02 19:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_alter_comment_owner_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='user_favs', to=settings.AUTH_USER_MODEL),
        ),
    ]
