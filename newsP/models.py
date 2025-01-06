from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=2, choices=(("1",'Active'), ("2",'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="", null=True, blank=True)
    banner_path = models.ImageField(upload_to='news_bannner')
    status = models.IntegerField(default=0)  # Example field for status
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    subject = models.CharField(max_length=250, null=True)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.post.title}"