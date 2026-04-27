from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from .ai_scoring import score_lead


@receiver(post_save, sender=Lead)
def auto_score_lead(sender, instance, created, **kwargs):
    if created:
        score_lead(instance)