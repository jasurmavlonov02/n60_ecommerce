from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from customer.models import Customer


@receiver(post_save, sender=Customer)
def create_customer(sender, instance, created, **kwargs):
    if created:
        pass
