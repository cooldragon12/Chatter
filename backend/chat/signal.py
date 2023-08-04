from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Message, Room, User
# When the user leaves
@receiver(post_save, sender=Room)
def when_user_joined(sender, **kwargs):
    pass

# When user enters