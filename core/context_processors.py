from django.conf import settings

def pwa_settings(request):
    """Expose PWA and push notification settings to templates."""
    return {
        'VAPID_PUBLIC_KEY': getattr(settings, 'VAPID_PUBLIC_KEY', ''),
    }

def monetization_settings(request):
    """Expose monetization settings to templates."""
    return {
        'ENABLE_ADSENSE': getattr(settings, 'ENABLE_ADSENSE', False),
        'GOOGLE_ADSENSE_CLIENT_ID': getattr(settings, 'GOOGLE_ADSENSE_CLIENT_ID', ''),
        'ENABLE_DONATIONS': getattr(settings, 'ENABLE_DONATIONS', False),
        'STRIPE_PUBLIC_KEY': getattr(settings, 'STRIPE_PUBLIC_KEY', ''),
    }
