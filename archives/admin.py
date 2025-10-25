from django.contrib import admin
from .models import Category, Archive

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive_type', 'category', 'uploaded_by', 'created_at', 'is_featured']
    list_filter = ['archive_type', 'category', 'is_featured']
    search_fields = ['title', 'description']
