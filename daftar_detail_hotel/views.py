from django.shortcuts import render

# Create your views here.

def get_daftar_hotel(request):
    return render(request, 'daftar_hotel.html')

def get_detail_hotel(request):
    return render(request, 'detail_hotel.html')