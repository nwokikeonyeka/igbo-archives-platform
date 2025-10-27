from notifications.signals import notify
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_post_approved_notification(post, post_type='insight'):
    """Send notification when a post is approved"""
    author = post.author if hasattr(post, 'author') else post.reviewer
    
    # In-app notification
    notify.send(
        sender=post,
        recipient=author,
        verb='approved your post',
        description=f'Your {post_type} "{post.title if hasattr(post, "title") else post.review_title}" has been approved and is now published!',
        action_object=post
    )
    
    # Email notification
    subject = f'Your {post_type.title()} has been approved!'
    message = f'Congratulations! Your {post_type} "{post.title if hasattr(post, "title") else post.review_title}" has been approved and is now live on Igbo Archives.'
    send_email_notification(author.email, subject, message)


def send_post_rejected_notification(post, reason, post_type='insight'):
    """Send notification when a post is rejected"""
    author = post.author if hasattr(post, 'author') else post.reviewer
    
    # In-app notification
    notify.send(
        sender=post,
        recipient=author,
        verb='rejected your post',
        description=f'Your {post_type} "{post.title if hasattr(post, "title") else post.review_title}" was not approved. Reason: {reason}',
        action_object=post
    )
    
    # Email notification
    subject = f'Your {post_type.title()} needs revision'
    message = f'Your {post_type} "{post.title if hasattr(post, "title") else post.review_title}" was not approved.\n\nReason: {reason}\n\nYou can revise and resubmit it from your dashboard.'
    send_email_notification(author.email, subject, message)


def send_new_comment_notification(comment, post):
    """Send notification when someone comments on your post"""
    post_author = post.uploaded_by if hasattr(post, 'uploaded_by') else (post.author if hasattr(post, 'author') else post.reviewer)
    
    # Don't notify if commenting on own post
    if comment.user and comment.user == post_author:
        return
    
    # In-app notification
    notify.send(
        sender=comment.user if comment.user else comment,
        recipient=post_author,
        verb='commented on your post',
        description=f'{comment.user.full_name if comment.user else comment.name} commented on your post',
        action_object=post
    )


def send_comment_reply_notification(comment, parent_comment):
    """Send notification when someone replies to your comment"""
    if not parent_comment.user:
        return  # Can't notify guest users
    
    # Don't notify if replying to own comment
    if comment.user and comment.user == parent_comment.user:
        return
    
    # In-app notification
    notify.send(
        sender=comment.user if comment.user else comment,
        recipient=parent_comment.user,
        verb='replied to your comment',
        description=f'{comment.user.full_name if comment.user else comment.name} replied to your comment',
        action_object=comment
    )


def send_message_notification(message, recipient):
    """Send notification when someone sends you a message"""
    # In-app notification
    notify.send(
        sender=message.sender,
        recipient=recipient,
        verb='sent you a message',
        description=f'{message.sender.full_name} sent you a message',
        action_object=message.thread
    )
    
    # Email notification
    subject = f'New message from {message.sender.full_name}'
    email_message = f'{message.sender.full_name} sent you a message on Igbo Archives.\n\nSubject: {message.thread.subject}\n\nLog in to read and reply: {settings.SITE_URL if hasattr(settings, "SITE_URL") else ""}/profile/messages/{message.thread.id}/'
    send_email_notification(recipient.email, subject, email_message)


def send_edit_suggestion_notification(suggestion):
    """Send notification when someone suggests an edit to your post"""
    post_author = suggestion.post.author
    suggester = suggestion.suggested_by
    
    # Don't notify if suggesting edit on own post
    if suggester == post_author:
        return
    
    # In-app notification
    notify.send(
        sender=suggester,
        recipient=post_author,
        verb='suggested an edit to your post',
        description=f'{suggester.full_name} suggested an edit to "{suggestion.post.title}"',
        action_object=suggestion
    )
    
    # Email notification
    subject = f'Edit suggestion on your post'
    message = f'{suggester.full_name} suggested an edit to your post "{suggestion.post.title}".\n\nSuggestion: {suggestion.suggestion_text}\n\nReview and approve or reject from your dashboard.'
    send_email_notification(post_author.email, subject, message)


def send_edit_suggestion_approved_notification(suggestion):
    """Send notification when your edit suggestion is approved"""
    # In-app notification
    notify.send(
        sender=suggestion.post.author,
        recipient=suggestion.suggested_by,
        verb='approved your edit suggestion',
        description=f'Your edit suggestion for "{suggestion.post.title}" was approved. You can now edit the post.',
        action_object=suggestion.post
    )


def send_edit_suggestion_rejected_notification(suggestion, reason=''):
    """Send notification when your edit suggestion is rejected"""
    # In-app notification
    notify.send(
        sender=suggestion.post.author,
        recipient=suggestion.suggested_by,
        verb='declined your edit suggestion',
        description=f'Your edit suggestion for "{suggestion.post.title}" was declined. {reason}',
        action_object=suggestion.post
    )


def send_email_notification(to_email, subject, message):
    """Helper function to send email notifications"""
    if not settings.EMAIL_BACKEND or 'console' in settings.EMAIL_BACKEND:
        # Email not configured, skip
        return
    
    try:
        send_mail(
            subject=f'Igbo Archives - {subject}',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
            fail_silently=True,
        )
    except Exception:
        # Fail silently to not disrupt user experience
        pass
