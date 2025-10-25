from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<str:username>/', views.profile_view, name='profile'),
    path('<str:username>/edit/', views.profile_edit, name='profile_edit'),
    path('messages/', views.message_inbox, name='inbox'),
    path('messages/<int:thread_id>/', views.message_thread, name='thread'),
    path('messages/compose/<str:username>/', views.compose_message, name='compose'),
]
