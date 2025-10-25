from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from .models import Message
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Message)
def notify_message_recipient(sender, instance, created, **kwargs):
    """
    Send notification when a new message is received.
    """
    if created:
        # Get all participants in the thread except the sender
        recipients = instance.thread.participants.exclude(id=instance.sender.id)
        
        for recipient in recipients:
            try:
                # Send in-app notification
                notify.send(
                    sender=instance.sender,
                    recipient=recipient,
                    verb='sent you a message',
                    target=instance.thread,
                    description=f'{instance.sender.username} sent you a message in "{instance.thread.subject}"'
                )
                logger.info(f"Message notification sent to {recipient.username}")
            except Exception as e:
                logger.error(f"Error sending message notification: {str(e)}")
