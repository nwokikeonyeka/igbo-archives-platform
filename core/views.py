from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Subscriber
from .forms import SubscriberForm


def home(request):
    return render(request, 'core/home.html')


@require_http_methods(["POST"])
def subscribe(request):
    """Handle newsletter subscription"""
    email = request.POST.get('email')
    
    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)
    
    # Check if already subscribed
    if Subscriber.objects.filter(email=email).exists():
        return JsonResponse({'message': 'You are already subscribed!'})
    
    try:
        Subscriber.objects.create(email=email, is_active=True)
        return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
