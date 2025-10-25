from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from .models import InsightPost, EditSuggestion
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=InsightPost)
def handle_insight_post_approval(sender, instance, created, **kwargs):
    """
    Signal handler for InsightPost save.
    Logs when a post is approved and published.
    """
    if not created and instance.is_approved and instance.is_published:
        if not instance.posted_to_social:
            logger.info(f"Post approved: {instance.title}")


@receiver(post_save, sender=EditSuggestion)
def notify_author_of_suggestion(sender, instance, created, **kwargs):
    """
    Notify the post author when someone suggests an edit.
    """
    if created and instance.post.author:
        try:
            notify.send(
                sender=instance.suggested_by if instance.suggested_by else instance.post.author,
                recipient=instance.post.author,
                verb='suggested an edit for',
                target=instance.post,
                description=f'{instance.suggested_by.full_name if instance.suggested_by else "A guest"} suggested an edit for your post "{instance.post.title}"'
            )
            logger.info(f"Notification sent to {instance.post.author.full_name} for edit suggestion")
        except Exception as e:
            logger.error(f"Error sending edit suggestion notification: {str(e)}")
