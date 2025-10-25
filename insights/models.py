from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()

class InsightPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field('Content', config_name='extends')
    excerpt = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(upload_to='insights/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insights')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    posted_to_social = models.BooleanField(default=False)
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class EditSuggestion(models.Model):
    post = models.ForeignKey(InsightPost, on_delete=models.CASCADE, related_name='suggestions')
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    suggestion_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Suggestion for {self.post.title}"
