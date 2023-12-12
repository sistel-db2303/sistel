from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .queries import login

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = login(email, password)
            
        if len(user[0]) == 0:
            context = {'login_error': 'Invalid login credentials'}
            return render(request, 'login.html', context)


        if len(user[1]) != 0:
            response = HttpResponseRedirect(reverse("r_dashboard:show_customer_dashboard"))
            response.set_cookie('email', user[0][0][0])
            response.set_cookie('role', 'customer')
            response.set_cookie('fname', user[0][0][2])
            response.set_cookie('lname', user[0][0][3])
            return response
        elif len(user[2]) != 0:
            response = HttpResponseRedirect(reverse("r_dashboard:show_hotel_dashboard"))
            response.set_cookie('email', user[0][0][0])
            response.set_cookie('role', 'hotel')
            return response


    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    response = HttpResponseRedirect(reverse('authentication:login_user'))
    response.delete_cookie('email')
    response.delete_cookie('role')
    response.delete_cookie('fname')
    response.delete_cookie('lname')
    return response

def register_user(request):
    #TODO: BUAT FUNGSI REGISTER
    return


users = [
    {'email': 'user1@example.com', 'password': 'password1', 'role': 'customer', 'id': 1},
    {'email': 'user2@example.com', 'password': 'password2', 'role': 'hotel', 'id': 2},
]

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Validasi login
#         user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        
#         if user:
#             # Simpan session untuk pengguna yang berhasil login
#             request.session['user_id'] = user['id']
#             if user['role'] == 'customer':
#                 return redirect('customer_dashboard')  # Redirect ke dashboard customer
#             elif user['role'] == 'hotel':
#                 return redirect('hotel_dashboard')  # Redirect ke dashboard hotel
#         else:
#             error_message = "Email atau password salah. Silakan coba lagi."
#             return render(request, 'login.html', {'error_message': error_message})
    
#     return render(request, 'login.html')

