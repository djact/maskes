from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import UserProfile, UserAddress
from supports.models import Request
from offers.models import Offer

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# @receiver(post_save, sender=User)
# def create_offer(sender, instance, created, **kwargs):
#     i = instance
#     if created and instance:
#         print(i)
#         Offer.objects.create()


@receiver(post_save, sender=Request)
def create_address(sender, instance, created, **kwargs):
    if created:
        UserAddress.objects.update_or_create(
            user = instance.requester,
            address1 = instance.address1,
            address2 = instance.address2,
            city =  instance.city,
            zip_code = instance.zip_code
        )