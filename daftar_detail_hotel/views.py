from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .queries import *

# Create your views here.

def show_daftar_hotel(request):
    try:
        email_user = request.COOKIES['email']
        fname_user = request.COOKIES['fname']
        lname_user = request.COOKIES['lname']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            minPrice = form.cleaned_data['minPrice']
            maxPrice = form.cleaned_data['maxPrice']
            hotels = get_hotels(minPrice, maxPrice)
            context = {
                "form" : form,
                "hotel_list" : hotels
            }
            return render(request, "daftar_hotel.html", context)
    else:
        form = SearchForm()
    context = {
        "email" : email_user,
        "fname" : fname_user,
        "lname" : lname_user,
        "form"  : form,
    }
    return render(request, 'daftar_hotel.html', context)

def show_detail_hotel(request, hotel_name):
    try:
        email_user = request.COOKIES['email']
        fname_user = request.COOKIES['fname']
        lname_user = request.COOKIES['lname']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    
    hotel_detail = get_hotel_detail(hotel_name)
    room_list = get_room_list(hotel_name)
    context = {
        "hotel_detail" : hotel_detail,
        "room_list" : room_list
    }

    return render(request, 'detail_hotel.html', context)