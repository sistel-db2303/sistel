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

def get_hotels(minPrice, maxPrice):
    conn = initalize_connection()
    cur = conn.cursor()

    cur.execute(rf"""
    
    SET search_path TO sistel;
    SELECT DISTINCT h.hotel_name, h.rating FROM hotel h
    JOIN room r ON r.hotel_name = h.hotel_name
    WHERE (price BETWEEN {minPrice} AND {maxPrice})
    ORDER BY h.hotel_name ASC;

    """)

    hotels = cur.fetchall()
    return hotels

def get_hotel_detail(hotel_name):
    conn = initalize_connection()
    cur = conn.cursor()

    cur.execute(rf"""
    
    SET search_path TO sistel;
    SELECT hotel_name, description, nib, rating, street, district, city, province, min_checkout, max_checkout
    FROM hotel WHERE hotel_name = '{hotel_name}';

    """)

    hotel_details = cur.fetchall()

    return hotel_details

def get_room_list(hotel_name):
    conn = initalize_connection()
    cur = conn.cursor()

    cur.execute(rf"""
    
    SET search_path TO sistel;
    SELECT r.number, r.price FROM room r
    JOIN room_facilities rf ON r.number = rf.rnum
    WHERE r.hotel_name = '{hotel_name}';

    """)

    room_list = cur.fetchall()

    return room_list