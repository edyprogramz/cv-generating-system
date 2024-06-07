from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from client.models import Client

@receiver(pre_save, sender=Client)
def update_subscription_status(sender, instance, **kwargs):
    if not instance.has_paid:
        instance.subscription_expires = None
    elif instance.subscription_expires is None or instance.subscription_expires <= timezone.now():
        instance.subscription_expires = timezone.now() + timedelta(weeks=2)
