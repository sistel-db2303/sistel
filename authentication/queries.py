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



def login(email, password):
    result = []
    conn = initalize_connection()
    cur = conn.cursor()
    cur.execute(rf"""
        set search_path to sistel;        
        
        select * from sistel.user
        where sistel.user.email = '{email}'
            and sistel.user.password = '{password}'

                """)
    
    
    user_data = cur.fetchall()
    result.append(user_data)

    cur.execute(rf"""
    set search_path to sistel;        

    select * from customer where customer.email = '{email}'

            """)
    
    customer_data = cur.fetchall()
    result.append(customer_data)

    cur.execute(rf"""
    set search_path to sistel;        

    select * from hotel where hotel.email = '{email}'

            """)
    
    hotel_data = cur.fetchall()
    result.append(hotel_data)

    return result


 
# executing queries to create table

