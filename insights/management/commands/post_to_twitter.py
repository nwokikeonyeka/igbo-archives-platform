from django.core.management.base import BaseCommand
from insights.models import InsightPost
import tweepy
from django.conf import settings

class Command(BaseCommand):
    help = 'Post approved insights to Twitter'
    
    def handle(self, *args, **options):
        if not all([settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET, 
                    settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET]):
            self.stdout.write(self.style.WARNING('Twitter API credentials not configured'))
            return
        
        client = tweepy.Client(
            consumer_key=settings.TWITTER_API_KEY,
            consumer_secret=settings.TWITTER_API_SECRET,
            access_token=settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )
        
        posts = InsightPost.objects.filter(
            is_published=True,
            is_approved=True,
            posted_to_social=False
        )[:5]
        
        for post in posts:
            try:
                tweet_text = f"{post.title}\n\n{post.excerpt[:200]}...\n\n#Igbo #IgboArchives\n\nhttps://igboarchives.com/insights/{post.slug}/"
                
                client.create_tweet(text=tweet_text)
                
                post.posted_to_social = True
                post.save()
                
                self.stdout.write(self.style.SUCCESS(f'Posted: {post.title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error posting {post.title}: {str(e)}'))
