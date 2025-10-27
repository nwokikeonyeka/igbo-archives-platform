from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from notifications.models import Notification
from django.http import JsonResponse


@login_required
def notifications_list(request):
    """Display all notifications for the logged-in user"""
    notifications = request.user.notifications.all()
    
    # Filter by read/unread
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'unread':
        notifications = notifications.unread()
    elif filter_type == 'read':
        notifications = notifications.read()
    
    # Paginate
    paginator = Paginator(notifications, 20)
    page = request.GET.get('page')
    notifications = paginator.get_page(page)
    
    context = {
        'notifications': notifications,
        'filter_type': filter_type,
    }
    
    return render(request, 'users/notifications.html', context)


@login_required
def notification_mark_read(request, notification_id):
    """Mark a single notification as read"""
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.mark_as_read()
    
    if request.htmx:
        return JsonResponse({'status': 'success'})
    
    return redirect('users:notifications')


@login_required
def notification_mark_all_read(request):
    """Mark all notifications as read"""
    request.user.notifications.mark_all_as_read()
    
    if request.htmx:
        return JsonResponse({'status': 'success'})
    
    return redirect('users:notifications')


@login_required
def notification_dropdown(request):
    """Return top 5 unread notifications for dropdown"""
    notifications = request.user.notifications.unread()[:5]
    unread_count = request.user.notifications.unread().count()
    
    context = {
        'notifications': notifications,
        'unread_count': unread_count,
    }
    
    return render(request, 'users/partials/notification_dropdown.html', context)
