from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('push-subscribe/', views.push_subscribe, name='push_subscribe'),
    path('push-unsubscribe/', views.push_unsubscribe, name='push_unsubscribe'),
    path('archive-media-browser/', views.archive_media_browser, name='archive_media_browser'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('get-categories/', views.get_categories, name='get_categories'),
]
