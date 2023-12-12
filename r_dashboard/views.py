from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
import json
from .queries import customer_dashboard_data, hotel_dashboard_data

# placeholder variable for logged_in_users
logged_in_user_email = 'ssupple5@about.com'

def show_customer_dashboard(request):
    try:
        user = request.COOKIES['email']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    data = customer_dashboard_data(user)
    context =  {
        'fname': data[0][0],
        'lname': data[0][1],
        'phonenum': data[0][2],
        'email': data[0][3],
        'nik': data[0][4],

    }
    return render(request, 'customer_dashboard.html', context)
    

def show_hotel_dashboard(request):
    try:
        user = request.COOKIES['email']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    data = hotel_dashboard_data(user)
    context = {
        'fname':data[0][0][0],
        'lname': data[0][0][1],
        'phonenum': data[0][0][2],
        'email': data[0][0][3],
        'nib': data[0][0][4],
        'hotel_name': data[0][0][5],
        'street': data[0][0][6],
        'city': data[0][0][7],
        'province': data[0][0][8],
        
        'room_data': data[1],
        'data_hotel_facilities': data[2]


    }
    return render(request, 'hotel_dashboard.html', context)
    