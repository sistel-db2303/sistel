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



def submit_complaint(email_user, hotel_name, hotel_branch, complaint):
    conn = initalize_connection()
    cur = conn.cursor()

    '''
    create or replace function cek_complaint()
    returns trigger as 
    $$
        declare
            rev_status varchar(50);
        begin
            if (tg_op = 'INSERT') then
                if (not exists(
                select status 
                from reservation_status, reservation_status_history, reservation
                where 
                    reservation.rID = new.rv_id
                    and reservation.rID = reservation_status_history.rID
                    and reservation_status_history.rsID = reservation_status.id;
                )) then
                raise exception 'Harus yang reservasinya aktif bang!';
                end if;
                return new;
            end if;
        end;
    $$
    Language plpgsql;

    '''


    '''
    create trigger trigger_cek_complaint
    before insert on complaints
    for each row
    execute procedure cek_complaint();
    '''

    cur.execute(rf"""
                
        set search_path to sistel;

        select reservation.rid 
        from reservation, reservation_room, room
        where reservation.cust_email = '{email_user}'
            and reservation.rid = reservation_room.rsv_id
            and reservation_room.rNum = room.number
            and room.hotel_name = '{hotel_name}'
            and room.hotel_branch = '{hotel_branch}'
                """)
    
    rev_id = cur.fetchall()[0][0]


    cur.execute (rf"""
        set search_path to sistel;
        
        select count(*) from complaints;
                 
                """)
    
    complaint_count = cur.fetchall()[0][0]
    

    cur.execute(rf"""
        set search_path to sistel;
                
        insert into complaints values
                ('CC{complaint_count+1}','{email_user}', '{rev_id}', '{complaint}');
                """
                )
    
    conn.commit()
    print('Successfully inserted complaint')


def submit_review(hotel_name, rating, review):
    return -1
