from django.urls import path
from CRU_Kamar_Hotel.views import tambah_kamar,daftar_kamar,kamar_tidak_ada,delete_room_view



app_name = 'CRU_Kamar_Hotel'


urlpatterns = [
    path('form-tambah-kamar', tambah_kamar, name = 'show_tambahKamar'),
    path('kamar-Hotel', daftar_kamar, name = 'show_daftarKamar'),
    path('kamar-Hotel-Tidak-Ada', kamar_tidak_ada, name = 'show_kamarTidakAda'),
    path('delete-room', delete_room_view, name = 'delete_room'),
]
