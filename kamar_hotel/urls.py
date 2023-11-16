from django.urls import path
from .views import *

urlpatterns = [
    path('', get_daftar_reservasi, name='get-daftar-reservasi'),
    path('update/', update_reservasi, name='update-reservasi'),
    path('get-detail/', get_detail_reservasi, name='get-detail-reservasi'),
    path('reservasi-shuttle/', reservasi_shuttle, name='reservasi-shuttle')
]