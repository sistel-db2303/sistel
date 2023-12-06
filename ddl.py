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
cur.execute(r"""

            set search_path to sistel;
select * from complaints
            
""")

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
