from django.shortcuts import render
from .forms import ComplaintForm, ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .queries import submit_complaint

def show_complaint_form(request):
    try:
        email_user = request.COOKIES['email']
        fname_user = request.COOKIES['fname']
        lname_user = request.COOKIES['lname']
    except:
        return HttpResponseRedirect(reverse("authentication:login_user"))
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            hotel_name = form.cleaned_data['nama_hotel']
            hotel_branch = form.cleaned_data['cabang_hotel']
            description = form.cleaned_data['description']
            try:
                submit_complaint(email_user, hotel_name, hotel_branch, description)
            except:
                context = {
                    "email" : email_user,
                    "fname" : fname_user,
                    "lname" : lname_user,
                    "form"  : form,
                    "error_message" : '''Terjadi kesalahan. Pastikan input hotel dan cabang hotel benar,
                                      customer memiliki reservasi yang aktif pada hotel tersebut. Terima kasih :)'''
                }
                return render(request, "complaint_form.html", context)
            return HttpResponseRedirect(reverse("r_dashboard:show_customer_dashboard"))


    else:
        form = ComplaintForm()
    context = {
        "email" : email_user,
        "fname" : fname_user,
        "lname" : lname_user,
        "form"  : form,
    }
    return render(request, "complaint_form.html", context)


def show_review_form(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = ReviewForm()
            form.save()
            #return redirect(TODO: Insert User DashBoard Page here)

    else:
        form = ReviewForm()
    context = {
        "email" : "contoh@email.com",
        "nama" : "Contoh Nama",
        "form" : form,
    }
    return render(request, "review_form.html", context)


