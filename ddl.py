import psycopg2
 
DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'bGfD-1fc22D*4fDEC4-d331f-25c6bbe'
DB_HOST = 'monorail.proxy.rlwy.net'
DB_PORT = '59422'
conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
print("Database connected successfully")
 
cur = conn.cursor()  # creating a cursor
 
# executing queries to create table
# cur.execute(rf"""
                
#         set search_path to sistel;

#         select room.number,room.price,room.floor,string_agg(room_facilities.id,', ')
#         from room,room_facilities   
#         where room.number = room_facilities.rNum
#         GROUP BY room.number,room.price,room.floor
#                 """)

cur.execute(rf"""
            
        set search_path to sistel;
        
        
        DROP TRIGGER IF EXISTS check_positive_values ON ROOM;

            
                """)

# cur.execute(rf"""
#                 set search_path to sistel;
#                 select * from room;

#             """)

data_kamar =  cur.fetchall()
print(data_kamar)

# commit the changes
conn.commit()
print("Task finished successfully")




'''
select status 
from reservation_status, reservation_status_history, reservation, complaints
where 
    reservation.rID = reservation_status_history.rID
    and reservation_status_history.rsID = reservation_status.id;
    '''
