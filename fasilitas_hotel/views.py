from django.shortcuts import render
from .forms import AddFasilitasForm
from django.http import HttpResponseRedirect
from .queries import submit_fasilitas, get_fasilitas, get_hotel_by_email, update_fasilitas, delete_fasilitas
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode

# Create your views here.

def fasilitas_hotel(request):
    email = request.COOKIES.get('email')
    hotel = get_hotel_by_email(email)
    facilities = get_fasilitas(nama_hotel=hotel.get('hotel_name'), hotel_branch=hotel.get('hotel_branch'))

    context = {
        'data': hotel,
        'facilities': facilities
    }

    return render(request, 'fasilitas_hotel.html', context)


@csrf_exempt
def add_fasilitas_hotel(request):
    if request.method == 'POST':
        email = request.COOKIES.get('email')
        hotel = get_hotel_by_email(email)
        nama_fasilitas = request.POST['nama_fasilitas']
        submit_fasilitas(hotel.get('hotel_name'), hotel.get('hotel_branch'), nama_fasilitas)
        return redirect('fasilitas_hotel:fasilitas_hotel')
    else:
        return render(request, 'add_fasilitas.html')


@csrf_exempt
def update_fasilitas_hotel(request):
    if request.method == 'POST':
        email = request.COOKIES.get('email')
        hotel = get_hotel_by_email(email)
        new_fasilitas = request.POST['new_fasilitas']
        old_fasilitas = request.POST['old_fasilitas']
        update_fasilitas(hotel.get('hotel_name'), hotel.get('hotel_branch'), old_fasilitas, new_fasilitas)
        return redirect('fasilitas_hotel:fasilitas_hotel')
    else:
        fasilitas = request.GET.get('fasilitas')
        return render(request, 'edit_fasilitas.html', {'fasilitas': fasilitas})
    

@csrf_exempt
def delete_fasilitas_hotel(request, nama_fasilitas):
    email = request.COOKIES.get('email')
    hotel = get_hotel_by_email(email)
    delete_fasilitas(hotel.get('hotel_name'), hotel.get('hotel_branch'), nama_fasilitas)
    return redirect('fasilitas_hotel:fasilitas_hotel')


# def show_fasilitas(request):
#     email = request.COOKIES.get('email')
#     hotel = get_hotel_by_email(email)
#     facilities = get_fasilitas(hotel.get('hotel_name'), hotel.get('hotel_branch'))
#     context = {
#         'facilities': facilities
#     }
    
#     return HttpResponse(context)