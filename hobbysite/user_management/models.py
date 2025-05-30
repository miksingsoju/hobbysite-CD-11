from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField(unique=True)
    bio           = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.display_name or self.user.username
