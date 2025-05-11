from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField(unique=True)
    # Added for fun
    bio = models.CharField(max_length=100)
    
    def __str__(self):
        return self.display_name