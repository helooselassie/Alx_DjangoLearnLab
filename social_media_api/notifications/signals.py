from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification, Like
from .models import Notification, Follow

@receiver(post_save, sender=Follow)
def generate_notification_on_follow(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.followed_user,
            actor=instance.user,
            verb='started following',
            target=instance.followed_user
        )
@receiver(post_save, sender=Like)
def generate_notification_on_like(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.user,
            actor=instance.user,
            verb='liked your post',
            target=instance.post
        )

def some_function():
    from .models import Notification, Follow        