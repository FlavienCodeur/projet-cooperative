from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image, ImageOps
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.jpg', upload_to='profile_avatars')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)