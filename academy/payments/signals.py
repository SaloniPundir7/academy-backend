from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Payment

@receiver(post_save, sender=Payment)
def clear_payment_cache_on_save(sender, instance, **kwargs):
    cache.delete(f"payments_{instance.user.id}")
    print("Cache cleared after SAVE ✅")


@receiver(post_delete, sender=Payment)
def clear_payment_cache_on_delete(sender, instance, **kwargs):
    cache.delete(f"payments_{instance.user.id}")
    print("Cache cleared after DELETE ✅")