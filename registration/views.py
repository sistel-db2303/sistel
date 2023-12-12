from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Customer, Hotel

def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'customer':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('login.html')
        elif role == 'hotel':
            form = HotelForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('login.html')
    else:
      
        return render(request, 'registration_form.html')
