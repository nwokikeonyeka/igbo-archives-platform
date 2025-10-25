from django.urls import path
from . import views

app_name = 'ai_service'

urlpatterns = [
    path('', views.ai_chat, name='chat'),
    path('api/', views.ai_chat_api, name='chat_api'),
]
