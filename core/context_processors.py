from django.conf import settings

def pwa_settings(request):
    """Expose PWA and push notification settings to templates."""
    return {
        'VAPID_PUBLIC_KEY': getattr(settings, 'VAPID_PUBLIC_KEY', ''),
    }
