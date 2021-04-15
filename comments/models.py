from django.db import models

from news.models import Post
from registration.models import BlogUser


class Comment(models.Model):
    body = models.CharField(max_length=127)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=BlogUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    parentComment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body
