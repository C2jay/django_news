from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profileimg = models.ImageField(upload_to='images', default='img.jpg')
    bio = models.TextField(max_length=1000, default="There is no bio yet!")

    def __str__(self):
        return self.username

