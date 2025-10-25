from django.contrib.sitemaps import Sitemap
from archives.models import Archive
from insights.models import InsightPost
from books.models import BookReview
from django.contrib.auth import get_user_model

User = get_user_model()

class ArchiveSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    
    def items(self):
        return Archive.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at

class InsightSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    
    def items(self):
        return InsightPost.objects.filter(is_published=True, is_approved=True)
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return f'/insights/{obj.slug}/'

class BookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    
    def items(self):
        return BookReview.objects.filter(is_published=True)
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return f'/books/{obj.slug}/'

class UserProfileSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    
    def items(self):
        return User.objects.filter(is_active=True)
    
    def location(self, obj):
        return f'/profile/{obj.username}/'
