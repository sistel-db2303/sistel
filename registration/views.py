from django.shortcuts import render
from .queries import insert_customer, insert_hotel
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

from django.http import HttpResponse
import psycopg2

def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        print(role)
        if role == 'customer':
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            phone_number = request.POST.get('phoneNumber')
            nik = request.POST.get('nik')
            try:
                insert_customer(email, password, first_name, last_name, phone_number, nik)
            except psycopg2.Error as e:
                print("Gagal menyimpan data Customer:", e)
                return render(request, 'register.html', {'error_message': 'Gagal register data. Silakan coba lagi.'})
            return HttpResponseRedirect(reverse("authentication:login_user"))


        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            owner_first_name = request.POST.get('ownerFirstName')
            owner_last_name = request.POST.get('ownerLastName')
            owner_phone_number = request.POST.get('ownerPhoneNumber')
            business_license = request.POST.get('businessLicense')
            hotel_name = request.POST.get('hotelName')
            hotel_branch = request.POST.get('hotelBranch')
            street_name = request.POST.get('streetName')
            district = request.POST.get('district')
            city = request.POST.get('city')
            province = request.POST.get('province')

            try:
                insert_hotel(email, password, owner_first_name, owner_last_name, owner_phone_number,
                 business_license, hotel_name, hotel_branch, street_name, district, city, province)
            except psycopg2.Error as e:
                print("Gagal menyimpan data Hotel:", e)
                return render(request, 'register.html', {'error_message': 'Gagal register data. Silakan coba lagi.'})
            return HttpResponseRedirect(reverse("authentication:login_user"))
    else:
      
        return render(request, 'register.html')
