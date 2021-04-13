from django.db import models
from django.contrib.auth.models import AbstractUser
from . import managers


class BlogUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.BlogUserManager()

    image = models.ImageField(default='/users/user.jpg', upload_to='')

    def __str__(self):
        return self.email
