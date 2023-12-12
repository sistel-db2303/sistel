from django.shortcuts import render

# Create your views here.

def show_fasilitas_hotel(request):
    return render(request, 'fasilitas_hotel.html')

def show_add_fasilitas_form(request):
    return render(request, 'add_fasilitas.html')

def show_update_fasilitas_form(request):
    return render(request, 'update_fasilitas.html')