from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()

class BookReview(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, blank=True)
    review_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field('Review Content', config_name='extends')
    rating = models.IntegerField(choices=RATING_CHOICES)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.book_title} - Review by {self.reviewer.username}"
