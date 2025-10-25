from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Archive(models.Model):
    ARCHIVE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
        ('artifact', 'Artifact'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    archive_type = models.CharField(max_length=20, choices=ARCHIVE_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        upload_to='archives/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])]
    )
    alt_text = models.CharField(max_length=255)
    date_created = models.DateField(null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
