from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
import uuid
from users.models import Profile

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    art_name = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='art_posts')
    favorites = models.ManyToManyField(User, related_name='user_favs', default=None, blank=True)

    def total_likes(self):
        return self.likes.all().count()

    
    def __str__(self):
        return str(self.art_name)

LIKE_CHOICES =(
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

def __str__(self):
        return str(self.id)