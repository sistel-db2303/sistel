from django.shortcuts import render

# Create your views here.

def get_fasilitas_hotel(request):
    return render(request, 'fasilitas_hotel.html')

def get_add_fasilitas(request):
    return render(request, 'add_fasilitas.html')

def get_update_fasilitas(request):
    return render(request, 'update_fasilitas.html')