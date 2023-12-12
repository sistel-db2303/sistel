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
            
    create or replace function cek_user()
    returns trigger as 
    $$
        declare
            rev_status varchar(50);
        begin
            if (tg_op = 'INSERT') then
                if (new.password ~* '[a-z]') is false or (new.password ~* '[0-9]') is false then
                raise exception 'Password harus mengandung angka dan huruf';
                end if;
                return new;
            end if;
        end;
    $$
    Language plpgsql;


            
                """)


# data_kamar =  cur.fetchall()
# print(data_kamar)

# commit the changes
# print(cur.fetchall())
conn.commit()
print("Task finished successfully")

