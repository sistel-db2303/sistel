from django.urls import path
from .views import *

app_name = "fasilitas_hotel"

urlpatterns = [
    path('', fasilitas_hotel, name='fasilitas_hotel'),
    path('show-fasilitas/', show_fasilitas, name = 'show_fasilitas'),
    path('add-fasilitas/', add_fasilitas_hotel, name='add_fasilitas_hotel'), 
    path('update-fasilitas/', update_fasilitas_hotel, name = 'update_fasilitas_hotel'),
    path('delete-fasilitas/<str:nama_fasilitas>', delete_fasilitas_hotel, name = 'delete_fasilitas_hotel'),
]