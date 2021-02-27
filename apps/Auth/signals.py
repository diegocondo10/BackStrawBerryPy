from django.db.models.signals import post_save
from django.dispatch import receiver
from graphql_auth.models import UserStatus


@receiver(post_save, sender=UserStatus)
def verify_account(sender, **kwargs):
    print(kwargs)
    pass
