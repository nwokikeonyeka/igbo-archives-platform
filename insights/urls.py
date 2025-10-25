from django.urls import path
from . import views

app_name = 'insights'

urlpatterns = [
    path('', views.insight_list, name='list'),
    path('create/', views.insight_create, name='create'),
    path('<slug:slug>/', views.insight_detail, name='detail'),
    path('<slug:slug>/suggest-edit/', views.suggest_edit, name='suggest_edit'),
]
