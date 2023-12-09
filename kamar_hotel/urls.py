from django.urls import path
from .views import *

urlpatterns = [
    path('', get_daftar_reservasi, name='get-daftar-reservasi'),
    path('update/<str:reservation_id>', update_reservasi, name='update-reservasi'),
    path('get-detail/<str:reservation_id>', get_detail_reservasi, name='get-detail-reservasi'),
    path('reservasi-shuttle/', reservasi_shuttle, name='reservasi-shuttle')
]