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

CREATE OR REPLACE FUNCTION CekStatusAktif ()
returns trigger as $$
DECLARE status_reservasi VARCHAR(20);
BEGIN


    -- Mendapatkan status reservasi kamar
    SELECT status INTO status_reservasi
    FROM reservation_status_history JOIN reservation_status ON rsid=id
    WHERE rid=new.rsv_id;

    -- Memeriksa apakah reservasi kamar aktif
    IF status_reservasi = 'aktif' THEN
        -- Insert ke dalam tabel ReservasiPenjemputan
	return new;
    ELSE
        RAISE EXCEPTION 'Status Reservasi Tidak Aktif';
    END IF;
END;
$$ language plpgsql;






            
""")


# commit the changes
# print(cur.fetchall())
conn.commit()
print("Task finished successfully")

