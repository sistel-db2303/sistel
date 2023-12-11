from django.urls import path
from .views import *

urlpatterns = [
    path('', get_daftar_hotel, name='get-daftar-hotel'),
    path('detail-hotel/', get_detail_hotel, name = 'get-detail-hotel')
]