from django.shortcuts import render

# Create your views here.

def get_daftar_reservasi(request):
    return render(request, 'daftar-reservasi-kamar.html')

def update_reservasi(request):
    return render(request, 'update-status-reservasi.html')

def get_detail_reservasi(request):
    return render(request, 'detail-reservasi.html')

def reservasi_shuttle(request):
    return render(request, 'reservasi-shuttle.html')
