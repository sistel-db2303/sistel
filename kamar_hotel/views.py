from django.shortcuts import render, redirect
import psycopg2
 
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

    cur.execute(f"""

    set search_path to sistel;
    select 1 from customer where email = '{email}';
                """)
    exist = cur.fetchone()
    if exist :
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

    # commit the changes
        conn.commit()
        context = {
            "result": data_reservasi,
            "is_hotel": is_hotel
        }
        return render(request, 'daftar-reservasi-kamar.html', context)
    
    else :
        cur.execute(f"""

        set search_path to sistel;
        select 1 from hotel where email = '{email}';
                    """)
        exist = cur.fetchone()
        
        if exist :
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
    if request.method == "POST":
        status_id = request.POST.get("status")
        cur.execute(f"""
        set search_path to sistel;
        update reservation_status_history
        set rsid = '{status_id}'
        where rid = '{reservation_id}';
        """)
        conn.commit()

        return redirect('get-detail-reservasi', reservation_id = reservation_id)

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
    email = request.COOKIES.get('email')
        
    cur.execute(f"""

    set search_path to sistel;
    select r.rid, rnum, hotel_name, hotel_branch, rsh.datetime, status
    from reservation r join reservation_room on r.rid = rsv_id
    join reservation_status_history rsh on r.rid = rsh.rid
    join reservation_status on rsid = id
    join room on rnum = number
    where cust_email = '{email}' and r.rid = '{reservation_id}';
                
    """)

    data_reservasi =  cur.fetchone()
    print(data_reservasi)
#('RSVP-01', 'Kamar 101', 'Hotel Aston', 'Jakarta', datetime.datetime(2022, 10, 19, 10, 0), 'Dalam Proses Konfirmasi')
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
    return render(request, 'detail-reservasi.html', context)


def reservasi_shuttle(request):
    return render(request, 'reservasi-shuttle.html')

# conn = psycopg2.connect(database=DB_NAME,
#                         user=DB_USER,
#                         password=DB_PASS,
#                         host=DB_HOST,
#                         port=DB_PORT)
# print("Database connected successfully")
 
# cur = conn.cursor()  # creating a cursor
 
# # executing queries to create table
# cur.execute(r"""

#             set search_path to sistel;
# select * from complaints
            
# """)

# data_kamar =  cur.fetchall()
# print(data_kamar)

# # commit the changes
# conn.commit()
# print("Task finished successfully")




# '''
# select status 
# from reservation_status, reservation_status_history, reservation, complaints
# where 
#     reservation.rID = reservation_status_history.rID
#     and reservation_status_history.rsID = reservation_status.id;
#     '''
