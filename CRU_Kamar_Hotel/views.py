from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .queries import add_room, get_hotel_info, show_room, delete_room

# View for the "Form Tambah Kamar" page
def tambah_kamar(request):
    user = ''
    nomor_kamar = ''
    harga = ''
    lantai = ''
    if request.method == 'POST':
        nomor_kamar = request.POST.get('nomorKamar')
        harga = request.POST.get('harga')
        lantai = request.POST.get('lantai')
        try:
            user = request.COOKIES['email']
            print('user : ',user)
        except:
            return HttpResponseRedirect(reverse("authentication:login_user"))
    else : return render(request, 'formTambahKamar.html')
    
    hotel_name,hotel_branch = get_hotel_info(user)
    print (request.method)

        # Panggil fungsi untuk menambahkan kamar
    add_room(nomor_kamar, harga, lantai, hotel_name, hotel_branch)  # Ganti dengan nama dan cabang hotel yang sesuai
        # Redirect atau render halaman setelah berhasil menambah kamar
        # TODO : CARI GANTI NAMA_HOTEL DAN CABANG_HOTEL

    return render(request, 'formTambahKamar.html')


# View for the "Kamar Hotel" page
def daftar_kamar(request):
    # Panggil fungsi untuk menampilkan daftar kamar
    daftar_kamar = show_room()  # Fungsi `show_room()` dari queries.py
    daftar_kamar_dict = []
    for row in daftar_kamar:
        kamar = {
            'Hotel_Name' : row[0],
            'Hotel_Branch' : row[1],
            'Nomor_Kamar': row[2],
            'Harga': row[3],
            'Lantai': row[4],
            'Daftar_Fasilitas': row[5],
        }
        daftar_kamar_dict.append(kamar)
    context = {
        "daftar_kamar": daftar_kamar_dict
    }
    return render(request, "kamarHotel.html", context)

# View for the "Kamar Hotel" page when there's no room available
def kamar_tidak_ada(request):
    return render(request, 'kamarHotelTidakAda.html')

def delete_room_view(request):
    # try:
    #     user = request.COOKIES['email']
    # except:
    #     return HttpResponseRedirect(reverse("authentication:login_user"))
    
    # hotel_name,hotel_branch = get_hotel_info(user)
    # print (request.method)

    if request.method == 'POST':
        Nomor_Kamar = request.POST.get('Nomor_Kamar')
        # print(Nomor_Kamar)
        Hotel_Name = request.POST.get('Hotel_Name')
        Hotel_Branch = request.POST.get('Hotel_Branch')
        delete_room(Nomor_Kamar,Hotel_Name,Hotel_Branch)  # Fungsi untuk menghapus kamar dari database
        return redirect('CRU_Kamar_Hotel:show_daftarKamar')  # Redirect kembali ke halaman daftar kamar


    return redirect('CRU_Kamar_Hotel:show_kamarTidakAda')  # Jika tidak ada POST request, redirect ke halaman lain


