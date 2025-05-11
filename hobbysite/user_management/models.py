from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name  = models.CharField(max_length=63)
    email_address = models.EmailField(unique=True)
    bio           = models.CharField(max_length=100, blank=True)

    def __str__(self):
        # human-readable representation
        return self.display_name or self.user.username

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Signal handler to ensure every User has a Profile.
    
    - When a User is first created, build a Profile with sensible defaults.
    - On every subsequent save, do a get_or_create so that orphaned users still get Profiles.
    """
    if created:
        Profile.objects.create(
            user=instance,
            display_name=instance.username,
            email_address=instance.email or ''
        )
    else:
        Profile.objects.get_or_create(user=instance)
