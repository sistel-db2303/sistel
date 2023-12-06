import psycopg2
 
DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'bGfD-1fc22D*4fDEC4-d331f-25c6bbe'
DB_HOST = 'monorail.proxy.rlwy.net'
DB_PORT = '59422'

def initalize_connection():
    return psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)



def customer_dashboard_data(email):
    conn = initalize_connection()
    cur = conn.cursor()
    cur.execute(rf"""
    set search_path to sistel;

    SELECT sistel.user.fname, sistel.user.lname, reservation_actor.phonenum, sistel.user.email, customer.nik
    FROM sistel.user, reservation_actor, customer
    WHERE sistel.user.email = '{email}' and sistel.user.email = reservation_actor.email
        and reservation_actor.email = customer.email
                """)
    
    return cur.fetchall()

def hotel_dashboard_data(email):
    result = []
    conn = initalize_connection()
    cur = conn.cursor()
    cur.execute(rf"""
        set search_path to sistel;
                
        select sistel.user.fname, sistel.user.lname, reservation_actor.phonenum, sistel.user.email,
                hotel.nib, hotel.hotel_name, hotel.street, hotel.city, hotel.province, hotel.hotel_branch
        from sistel.user, reservation_actor, hotel
        where sistel.user.email = '{email}' and sistel.user.email = reservation_actor.email
        and reservation_actor.email = hotel.email
                """)
    
    data_hotel = cur.fetchall()

    result.append(data_hotel)

    hotel_name = data_hotel[0][5]
    hotel_branch = data_hotel[0][9]

    cur.execute(rf"""
        set search_path to sistel;
        
        select room.number, room.price, room.floor, string_agg(room_facilities.id, ',')
        from room, room_facilities
        where room.number = room_facilities.rnum and room.hotel_name = room_facilities.hotel_name
                and room.hotel_branch = room_facilities.hotel_branch and room.hotel_name = '{hotel_name}'
                and room.hotel_Branch = '{hotel_branch}'
        group by room.number, room.price, room.floor;
                """)


    data_kamar =  cur.fetchall()
    result.append(data_kamar)

    cur.execute(rf"""
        set search_path to sistel;
                
        select hotel_facilities.facility_name
        from hotel_facilities, hotel
        where hotel.hotel_name = hotel_facilities.hotel_name
                and hotel.hotel_branch = hotel_facilities.hotel_branch
                and hotel.hotel_name = '{hotel_name}' and hotel.hotel_branch = '{hotel_branch}';
                """
                )
    
    data_hotel_facilities = cur.fetchall()
    result.append(data_hotel_facilities)

    return result


 
# executing queries to create table

