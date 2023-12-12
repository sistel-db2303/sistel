from django.urls import path
from .views import *

app_name = 'fasilitas_hotel'

urlpatterns = [
    path('', show_fasilitas_hotel, name='show_fasilitas_hotel'),
    path('add/', show_add_fasilitas_form, name = 'show_add_fasilitas_form'),
    path('update/', show_update_fasilitas_form, name = 'show_update_fasilitas_form'),
]