from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking


@receiver(post_save, sender=Booking)
def booking_created(sender, instance, created, **kwargs):
    if created:
        pass