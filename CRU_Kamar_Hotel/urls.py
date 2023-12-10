from django.urls import path
from CRU_Kamar_Hotel.views import show_formTambahKamar,show_kamarHotel,show_kamarHotelTidakAda,show_tambahFasilitasKamar

## NOTES : show_formTambahKamar,show_kamarHotel,show_kamarHotelTidakAda,show_tambahFasilitasKamar
##       : BELUM DIBIKIN FUNCTIONNYA

app_name = 'CRU_Kamar_Hotel'

urlpatterns = [
    path('form-tambah-kamar', show_formTambahKamar, name = 'show_formTambahKamar'),
    path('kamar-Hotel', show_kamarHotel, name = 'show_kamarHotel'),
    path('kamar-Hotel-Tidak-Ada', show_kamarHotelTidakAda, name = 'show_kamarHotelTidakAda'),
    path('tambah-Fasilitas-Kamar', show_tambahFasilitasKamar, name = 'show_tambahFasilitasKamar'),
]
