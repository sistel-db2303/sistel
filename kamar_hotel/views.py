from django.shortcuts import render, redirect
import psycopg2
from datetime import datetime, timedelta, timezone
from django.contrib import messages
 
DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'bGfD-1fc22D*4fDEC4-d331f-25c6bbe'
DB_HOST = 'monorail.proxy.rlwy.net'
DB_PORT = '59422'

# Create your views here.

def get_daftar_reservasi(request):
    conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
    cur = conn.cursor()
    email = request.COOKIES.get('email')
    role = request.COOKIES.get('role')

    if role == 'customer' :
        cur.execute(f"""

        set search_path to sistel;
        select r.rid, rnum, rsh.datetime, status
        from reservation r join reservation_room on r.rid = rsv_id
        join reservation_status_history rsh on r.rid = rsh.rid
        join reservation_status on rsid = id
        where cust_email = '{email}';
                    
        """)

        data_reservasi =  cur.fetchall()
        is_hotel = False

    
    else :
        cur.execute(f"""

        set search_path to sistel;
        select r.rid, rnum, rsh.datetime, status
        from reservation r join reservation_room on r.rid = rsv_id
        join reservation_status_history rsh on r.rid = rsh.rid
        join reservation_status on rsid = id
        join room ro on rnum = number
        join hotel h on (ro.hotel_name, ro.hotel_branch)=(h.hotel_name, h.hotel_branch)
        where email = '{email}';
                    
        """)

        data_reservasi =  cur.fetchall()
        is_hotel = True

    conn.commit()
    context = {
        "result": data_reservasi,
        "is_hotel": is_hotel
    }
    return render(request, 'daftar-reservasi-kamar.html', context)


def update_reservasi(request, reservation_id):
    conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
    cur = conn.cursor()
    email = request.COOKIES.get('email')
    role = request.COOKIES.get('role')

    if role != 'hotel':
        return redirect('kamar_hotel:get-daftar-reservasi')
    
    if request.method == "POST":
        try:

            status_id = request.POST.get("status")
            cur.execute(f"""
            set search_path to sistel;
            update reservation_status_history
            set rsid = '{status_id}', datetime='{datetime.now(timezone(timedelta(hours=7)))}'
            where rid = '{reservation_id}';
            """)
            conn.commit()
        except Exception as e:
            messages.error(request,str(e))
        finally:
            return redirect('kamar_hotel:get-detail-reservasi', reservation_id = reservation_id)
        

    cur.execute(f"""
    
    set search_path to sistel;
    select r.rid, rnum, rsid
    from reservation r join reservation_room on r.rid = rsv_id
    join reservation_status_history rsh on r.rid = rsh.rid
    where r.rid = '{reservation_id}';
                
    """)

    data_reservasi = cur.fetchone()

    cur.execute(f"""

    set search_path to sistel;
    select * from reservation_status;

    """)

    daftar_status = cur.fetchall()
    context = {"id": data_reservasi[0],
               "nomor": data_reservasi[1],
               "status_id": data_reservasi[2],
               "daftar_status": daftar_status,
               "reservation_id": reservation_id
    }

    return render(request, 'update-status-reservasi.html', context)

def get_detail_reservasi(request, reservation_id):
    conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
    cur = conn.cursor()
        
    cur.execute(f"""

    set search_path to sistel;
    select r.rid, rnum, hotel_name, hotel_branch, rsh.datetime, status
    from reservation r join reservation_room on r.rid = rsv_id
    join reservation_status_history rsh on r.rid = rsh.rid
    join reservation_status on rsid = id
    join room on rnum = number
    where r.rid = '{reservation_id}';
                
    """)

    data_reservasi =  cur.fetchone()

    cur.execute(f"""

    set search_path to sistel;
    select vehicle_num, driver_phonenum, datetime
    from reservation_shuttleservice
    where rsv_id='{reservation_id}'
    ;
    """)

    data_shuttle = cur.fetchone()
    print(data_shuttle)
    print(reservation_id)

    # commit the changes
    conn.commit()
    context = {
        "id" : data_reservasi[0],
        "nomor" : data_reservasi[1],
        "nama_hotel" : data_reservasi[2],
        "cabang_hotel" : data_reservasi[3],
        "tanggal" : data_reservasi[4],
        "status" : data_reservasi[5]
    }

    if data_shuttle:
        context['nomor_kendaraan']=data_shuttle[0]
        context['nomor_driver']=data_shuttle[1]
        context['tanggal_shuttle']=data_shuttle[2]

    return render(request, 'detail-reservasi.html', context)


def reservasi_shuttle(request, reservation_id):
    conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
    cur = conn.cursor()
    email = request.COOKIES.get('email')
    role = request.COOKIES.get('role')

    # if role != 'customer':
    #     return redirect('get-daftar-reservasi')
    
    if request.method == "POST":
        try :

            key = eval(request.POST.get("shuttle_service"))
            print(key)
            cur.execute(f"""
            set search_path to sistel;
            insert into reservation_shuttleservice
            values ('{reservation_id}', '{key[0]}', '{key[1]}', '{datetime.now(timezone(timedelta(hours=7)))}', true);
            """)
            conn.commit()

        except Exception as e:
            messages.error(request, str(e))
        finally:
            return redirect('kamar_hotel:get-detail-reservasi', reservation_id = reservation_id)
            

    cur.execute(f"""

    set search_path to sistel;
    select driver_name, vehicle_brand, vehicle_type, phonenum, platnum
    from shuttle_service join driver on driver_phonenum=phonenum
    join vehicle on vehicle_platnum=platnum;

    """)

    daftar_shuttle_service = cur.fetchall()
    context = {"daftar_shuttle_service": daftar_shuttle_service,
               "reservation_id": reservation_id

    }

    return render(request, 'reservasi-shuttle.html', context)