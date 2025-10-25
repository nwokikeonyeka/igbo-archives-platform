from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('push-subscribe/', views.push_subscribe, name='push_subscribe'),
    path('push-unsubscribe/', views.push_unsubscribe, name='push_unsubscribe'),
]
