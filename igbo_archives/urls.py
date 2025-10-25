from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('users.urls')),
    path('archives/', include('archives.urls')),
    path('insights/', include('insights.urls')),
    path('books/', include('books.urls')),
    path('ai-chat/', include('ai_service.urls')),
    path('comments/', include('django_comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
