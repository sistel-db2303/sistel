from django.shortcuts import render
from .forms import ComplaintForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def show_complaint_form(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form = ComplaintForm()
            form.save()
            #return redirect(TODO: Insert User DashBoard Page here)

    else:
        form = ComplaintForm()
    context = {
        "email" : "contoh@email.com",
        "nama" : "Contoh Nama",
        "form" : form,
    }
    return render(request, "complaint_form.html", context)

