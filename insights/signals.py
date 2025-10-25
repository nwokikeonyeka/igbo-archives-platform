from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail
from django.conf import settings
from django.template.loader import render_to_string
from notifications.signals import notify
from .models import InsightPost, EditSuggestion
from core.models import Subscriber
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=InsightPost)
def handle_insight_post_approval(sender, instance, created, **kwargs):
    """
    Signal handler for InsightPost save.
    Sends notifications and emails when a post is approved.
    """
    if not created and instance.is_approved and instance.is_published:
        # Check if this is a new approval (not already processed)
        if not instance.posted_to_social:
            # Send in-app notifications to followers (if applicable)
            # For now, just log the approval
            logger.info(f"Post approved: {instance.title}")
            
            # Send emails to subscribers
            try:
                send_subscriber_emails_for_post(instance)
            except Exception as e:
                logger.error(f"Error sending subscriber emails: {str(e)}")


def send_subscriber_emails_for_post(post):
    """
    Send email notifications to all active subscribers for a newly approved post.
    """
    subscribers = Subscriber.objects.filter(is_active=True)
    
    if not subscribers.exists():
        logger.info("No active subscribers to notify")
        return
    
    # Prepare email content
    subject = f'New on Igbo Archives: {post.title}'
    
    # Get the site domain (for production, this should come from settings or Site model)
    site_domain = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else 'igboarchives.com'
    post_url = f'https://{site_domain}/insights/{post.slug}/'
    
    message = f'''Hello,

A new article has been published on Igbo Archives:

{post.title}

{post.excerpt}

Read the full article at: {post_url}

Best regards,
Igbo Archives Team

---
To unsubscribe from these notifications, please visit your account settings.
'''
    
    # Prepare mass mailing
    messages = []
    for subscriber in subscribers:
        messages.append((
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email]
        ))
    
    # Send emails in batches to respect rate limits
    batch_size = 50
    total_sent = 0
    
    for i in range(0, len(messages), batch_size):
        batch = messages[i:i + batch_size]
        try:
            send_mass_mail(batch, fail_silently=False)
            total_sent += len(batch)
            logger.info(f"Sent {len(batch)} subscriber emails for post: {post.title}")
        except Exception as e:
            logger.error(f"Error sending email batch: {str(e)}")
    
    logger.info(f"Total subscriber emails sent: {total_sent} for post: {post.title}")


@receiver(post_save, sender=EditSuggestion)
def notify_author_of_suggestion(sender, instance, created, **kwargs):
    """
    Notify the post author when someone suggests an edit.
    """
    if created and instance.post.author:
        try:
            # Send in-app notification
            notify.send(
                sender=instance.suggested_by if instance.suggested_by else instance.post.author,
                recipient=instance.post.author,
                verb='suggested an edit for',
                target=instance.post,
                description=f'{instance.suggested_by.username if instance.suggested_by else "A guest"} suggested an edit for your post "{instance.post.title}"'
            )
            logger.info(f"Notification sent to {instance.post.author.username} for edit suggestion")
        except Exception as e:
            logger.error(f"Error sending edit suggestion notification: {str(e)}")
