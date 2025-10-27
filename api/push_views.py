from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from push_notifications.models import WebPushDevice
import json


@login_required
@require_POST
def push_subscribe(request):
    """Save push notification subscription for the user"""
    try:
        data = json.loads(request.body)
        
        # Create or update WebPush device
        device, created = WebPushDevice.objects.update_or_create(
            user=request.user,
            defaults={
                'registration_id': json.dumps(data),
                'p256dh': data.get('keys', {}).get('p256dh', ''),
                'auth': data.get('keys', {}).get('auth', ''),
            }
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Push subscription saved successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


@login_required
@require_POST
def push_unsubscribe(request):
    """Remove push notification subscription"""
    try:
        WebPushDevice.objects.filter(user=request.user).delete()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Push subscription removed successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
