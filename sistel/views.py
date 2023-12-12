from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from r_dashboard.views import show_customer_dashboard, show_hotel_dashboard

# Contoh data pengguna yang direpresentasikan dalam sebuah list


def show_main(request):
    try:
        role = request.COOKIES['role']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    
    if role == 'customer':
        return show_customer_dashboard(request)
    else:
        return show_hotel_dashboard(request)