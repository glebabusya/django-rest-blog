from django.db import models

from registration.models import BlogUser


class Post(models.Model):
    title = models.CharField(max_length=63)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=BlogUser, related_name='posts', on_delete=models.CASCADE)
    slug = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.title

    def generate_slug(self):
        author_username = str(self.author).split('@')

        return f'{author_username[0]}-{self.title}'


