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


def submit_fasilitas(nama_hotel, hotel_branch, nama_fasilitas):
    conn = initalize_connection()
    curr = conn.cursor()
    
    SET_SEARCH_PATH = f"SET SEARCH_PATH TO SISTEL; "
    insert_query = f"INSERT INTO HOTEL_FACILITIES VALUES(\'{nama_hotel}\', \'{hotel_branch}\', \'{nama_fasilitas}\');"
    query = SET_SEARCH_PATH + insert_query
    curr.execute(query)
    conn.commit()
    

def get_fasilitas(nama_hotel, hotel_branch):
    conn = initalize_connection()
    curr = conn.cursor()
    
    SET_SEARCH_PATH = f"SET SEARCH_PATH TO SISTEL; "
    fetch_query = f"SELECT * FROM HOTEL_FACILITIES AS HF WHERE HF.hotel_name=\'{nama_hotel}\' AND HF.hotel_branch=\'{hotel_branch}\';"
    query = SET_SEARCH_PATH + fetch_query

    curr.execute(query)
    data = curr.fetchall() #ngambil data
    conn.commit()
    
    res = []
    for row in data:
        res.append({
            'hotel_name': row[0],
            'hotel_branch': row[1],
            'facility': row[2]
        })
    return res


def get_hotel_by_email(email):
    conn = initalize_connection()
    curr = conn.cursor()
    
    SET_SEARCH_PATH = f"SET SEARCH_PATH TO SISTEL; "
    fetch_query = f""" SELECT * FROM HOTEL WHERE email = '{email}' """
    query = SET_SEARCH_PATH + fetch_query

    curr.execute(query)
    data = curr.fetchall()
    data = data[0]
    conn.commit()

    res = {
        'email': data[0],
        'hotel_name': data[1],
        'hotel_branch': data[2],
    }
    return res


def delete_fasilitas(nama_hotel, hotel_branch, nama_fasilitas):
    conn = initalize_connection()
    curr = conn.cursor()

    SET_SEARCH_PATH = f"SET SEARCH_PATH TO SISTEL; "
    delete_query = f"DELETE FROM HOTEL_FACILITIES WHERE hotel_name='{nama_hotel}' AND hotel_branch='{hotel_branch}' AND facility_name='{nama_fasilitas}';"
    query = SET_SEARCH_PATH + delete_query
    curr.execute(query)
    conn.commit()


def update_fasilitas(nama_hotel, hotel_branch, old_nama_fasilitas, new_nama_fasilitas):
    conn = initalize_connection()
    curr = conn.cursor()

    SET_SEARCH_PATH = f"SET SEARCH_PATH TO SISTEL; "
    update_query = f"UPDATE HOTEL_FACILITIES SET facility_name='{new_nama_fasilitas}' WHERE hotel_name='{nama_hotel}' AND hotel_branch='{hotel_branch}' AND facility_name='{old_nama_fasilitas}';"
    query = SET_SEARCH_PATH + update_query
    curr.execute(query)
    conn.commit()