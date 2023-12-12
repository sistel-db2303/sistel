"""
URL configuration for sistel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import show_main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('complaint_review.urls')),
    path('kamar-hotel/', include('kamar_hotel.urls')),
    path('dashboard/', include('r_dashboard.urls')),
    path('auth/', include('authentication.urls')),
    path('fasilitas-hotel/', include('fasilitas_hotel.urls')),
    path('CRU-Kamar-Hotel/', include('CRU_Kamar_Hotel.urls')),
    path('registration/', include('registration.urls')),
    path('', show_main, name='show_main'),
    path('daftar_hotel/', include('daftar_detail_hotel.urls')),
]
