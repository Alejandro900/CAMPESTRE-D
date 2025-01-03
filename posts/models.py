from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    image = models.ImageField(null=True)
    likes = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quote


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", null=True)
    text = models.TextField()
