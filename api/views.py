from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from push_notifications.models import WebPushDevice
import json

@csrf_exempt
@require_http_methods(["POST"])
def push_subscribe(request):
    """
    Handle push notification subscription from the client.
    Stores the subscription data using django-push-notifications.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    
    try:
        data = json.loads(request.body)
        
        # Extract subscription details
        endpoint = data.get('endpoint')
        p256dh = data.get('keys', {}).get('p256dh')
        auth = data.get('keys', {}).get('auth')
        
        if not all([endpoint, p256dh, auth]):
            return JsonResponse({'error': 'Invalid subscription data'}, status=400)
        
        # Create or update the device subscription
        device, created = WebPushDevice.objects.update_or_create(
            user=request.user,
            defaults={
                'registration_id': endpoint,
                'p256dh': p256dh,
                'auth': auth,
                'browser': request.META.get('HTTP_USER_AGENT', 'unknown')[:255],
            }
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Subscription saved' if created else 'Subscription updated'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["POST"])
def push_unsubscribe(request):
    """Remove push notification subscription."""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    
    WebPushDevice.objects.filter(user=request.user).delete()
    return JsonResponse({'success': True, 'message': 'Unsubscribed'})
