from django.contrib import admin
from django.urls import path,include
from .views import register

app_name = 'registration'

urlpatterns = [
    path('', register, name='register'),
    
]