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



def add_room(number,price,floor,hotel_name,hotel_branch):
    conn = initalize_connection()
    cur = conn.cursor()

    cur.execute(rf"""
        set search_path to sistel;
                
        insert into room values
                ('{hotel_name}','{hotel_branch}','{number}','{price}', '{floor}');
                """
                )
    
    conn.commit()
    print('Successfully inserted room')
    

def show_room(hotel_name,hotel_branch):
    conn = initalize_connection()
    cur = conn.cursor() 

    cur.execute(rf"""
                
        set search_path to sistel;

        select room.hotel_name,room.hotel_branch,room.number,room.price,room.floor,string_agg(room_facilities.id,', ')
        from room 
        LEFT JOIN room_facilities ON room.number = room_facilities.rNum
        where room.hotel_name = '{hotel_name}' AND room.hotel_branch = '{hotel_branch}'
        GROUP BY room.hotel_name,room.hotel_branch,room.number,room.price,room.floor
                """)
    
    rev_id = cur.fetchall()
    return rev_id

def delete_room(number,hotel_name,hotel_branch):
    conn = initalize_connection()
    cur = conn.cursor()

    cur.execute(rf"""
                
        set search_path to sistel;

        DELETE FROM room WHERE room.number = '{number}' AND room.hotel_name = '{hotel_name}' AND room.hotel_branch = '{hotel_branch}'        
                """)
    
    print(number,hotel_name,hotel_branch)

    conn.commit()
    cur.close()
    
    
    
def get_hotel_info(email):
    print('email : ', email)
    result = []
    conn = initalize_connection()
    cur = conn.cursor()
    cur.execute(rf"""
        set search_path to sistel;
                
        select hotel.hotel_name, hotel.hotel_branch
        from sistel.user, reservation_actor, hotel
        where sistel.user.email = '{email}' and sistel.user.email = reservation_actor.email
        and reservation_actor.email = hotel.email
    """)

    data_hotel = cur.fetchall()

    if data_hotel:  # Check if data_hotel has any rows
        hotel_name = data_hotel[0][0]
        hotel_branch = data_hotel[0][1]
        return hotel_name, hotel_branch
    else:
        # Handle the case where no data is retrieved for the provided email
        return None, None  # Return None or appropriate values as needed


    


   
    

    
