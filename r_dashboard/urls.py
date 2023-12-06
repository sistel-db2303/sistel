from django.urls import path
from .views import show_customer_dashboard, show_hotel_dashboard
app_name = 'r_dashboard'

urlpatterns = [
    path('customer', show_customer_dashboard, name='show_customer_dashboard'),
    path('hotel', show_hotel_dashboard, name='show_hotel_dashboard'),
]
