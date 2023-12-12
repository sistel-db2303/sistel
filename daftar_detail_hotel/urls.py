from django.urls import path
from .views import *

app_name = 'daftar_detail_hotel'

urlpatterns = [
    path('', show_daftar_hotel, name='show_daftar_hotel'),
    path('detail-hotel/<str:hotel_name>/', show_detail_hotel, name = 'show_detail_hotel')
]