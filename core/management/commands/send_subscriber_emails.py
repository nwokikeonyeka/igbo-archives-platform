from django.core.management.base import BaseCommand
from core.models import Subscriber
from insights.models import InsightPost
from django.core.mail import send_mass_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Send email notifications to subscribers for new posts'
    
    def handle(self, *args, **options):
        new_posts = InsightPost.objects.filter(
            is_published=True,
            is_approved=True,
            posted_to_social=False
        )
        
        if not new_posts.exists():
            self.stdout.write('No new posts to send')
            return
        
        subscribers = Subscriber.objects.filter(is_active=True)
        
        if not subscribers.exists():
            self.stdout.write('No active subscribers')
            return
        
        messages = []
        for post in new_posts:
            subject = f'New on Igbo Archives: {post.title}'
            message = f'''Hello,

A new article has been published on Igbo Archives:

{post.title}

{post.excerpt}

Read more at: https://igboarchives.com/insights/{post.slug}/

Best regards,
Igbo Archives Team
'''
            
            for subscriber in subscribers:
                messages.append((subject, message, settings.DEFAULT_FROM_EMAIL, [subscriber.email]))
        
        try:
            send_mass_mail(messages, fail_silently=False)
            self.stdout.write(self.style.SUCCESS(f'Sent {len(messages)} email(s)'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending emails: {str(e)}'))
