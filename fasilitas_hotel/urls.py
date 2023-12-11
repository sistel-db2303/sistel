from django.urls import path
from .views import *

urlpatterns = [
    path('', get_fasilitas_hotel, name='get-fasilitas-hotel'),
    path('add/', get_add_fasilitas, name = 'get-add-fasilitas'),
    path('update/', get_update_fasilitas, name = 'get-update-fasilitas'),
]