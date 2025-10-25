from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Thread, Message
from django.contrib import messages as django_messages

User = get_user_model()

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'profile_user': user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        request.user.full_name = request.POST.get('full_name', '')
        request.user.bio = request.POST.get('bio', '')
        if 'profile_picture' in request.FILES:
            request.user.profile_picture = request.FILES['profile_picture']
        request.user.save()
        django_messages.success(request, 'Profile updated successfully!')
        return redirect('users:profile', username=request.user.username)
    return render(request, 'users/profile_edit.html')

@login_required
def message_inbox(request):
    threads = request.user.message_threads.all()
    return render(request, 'users/inbox.html', {'threads': threads})

@login_required
def message_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, participants=request.user)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(thread=thread, sender=request.user, content=content)
            return redirect('users:thread', thread_id=thread_id)
    thread.messages.exclude(sender=request.user).update(is_read=True)
    return render(request, 'users/thread.html', {'thread': thread})

@login_required
def compose_message(request, username):
    recipient = get_object_or_404(User, username=username)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        if subject and content:
            thread = Thread.objects.create(subject=subject)
            thread.participants.add(request.user, recipient)
            Message.objects.create(thread=thread, sender=request.user, content=content)
            return redirect('users:thread', thread_id=thread.id)
    return render(request, 'users/compose.html', {'recipient': recipient})
