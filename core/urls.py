from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('terms/', views.terms_of_service, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('copyright/', views.copyright_policy, name='copyright'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
