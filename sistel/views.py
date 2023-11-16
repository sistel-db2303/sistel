from django.shortcuts import render, redirect

# Contoh data pengguna yang direpresentasikan dalam sebuah list
users = [
    {'email': 'user1@example.com', 'password': 'password1', 'role': 'customer', 'id': 1},
    {'email': 'user2@example.com', 'password': 'password2', 'role': 'hotel', 'id': 2},
]

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validasi login
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        
        if user:
            # Simpan session untuk pengguna yang berhasil login
            request.session['user_id'] = user['id']
            if user['role'] == 'customer':
                return redirect('customer_dashboard')  # Redirect ke dashboard customer
            elif user['role'] == 'hotel':
                return redirect('hotel_dashboard')  # Redirect ke dashboard hotel
        else:
            error_message = "Email atau password salah. Silakan coba lagi."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
