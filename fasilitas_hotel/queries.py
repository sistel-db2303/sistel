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

def submit_fasilitas (hotel_name, hotel_branch, facility_name):
    conn = initalize_connection()
    cur = conn.cursor()

    
    
    cur.execute(rf"""
    
    set search_path to sistel;
                
    insert into hotel_facilities values
                ('CC{facility_count+1}')
                """)



