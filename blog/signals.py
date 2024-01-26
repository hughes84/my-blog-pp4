from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# pylint: disable=no-member

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to create a user profile when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver function to save a user profile when a user is saved.
    """
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # If profile does not exist, create it
        Profile.objects.create(user=instance)
