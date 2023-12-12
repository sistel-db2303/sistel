import psycopg2
from django.shortcuts import render, redirect


DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'bGfD-1fc22D*4fDEC4-d331f-25c6bbe'
DB_HOST = 'monorail.proxy.rlwy.net'
DB_PORT = '59422'

'''
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

'''


'''
    create trigger trigger_cek_user
    before insert on sistel.user
    for each row
    execute procedure cek_user();
'''



def initialize_connection():
    return psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)

def insert_customer(email, password, first_name, last_name, phone_number, nik):
    connection = initialize_connection()
    cursor = connection.cursor()
    
    query = """
        set search_path to sistel;
        INSERT INTO sistel.user (email, password, fname, lname)
        VALUES (%s, %s, %s, %s);
        insert into reservation_actor (email, phonenum, admin_email)
        values (%s, %s, 'jbrackenridge0@stanford.edu');
        insert into customer (email, nik)
        values (%s, %s);
    """
    data = (email, password, first_name, last_name, email, phone_number, email, nik)

    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()

def insert_hotel(email, password, owner_first_name, owner_last_name, owner_phone_number,
                 business_license, hotel_name, hotel_branch, street_name, district, city, province):
    connection = initialize_connection()
    cursor = connection.cursor()
    
    query = """
        set search_path to sistel;
        insert into sistel.user (email, password, fname, lname)
        values (%s, %s, %s, %s);
        insert into reservation_actor (email, phonenum, admin_email)
        values (%s, %s, 'jbrackenridge0@stanford.edu');
        INSERT INTO sistel.hotel (email, hotel_name, hotel_branch, nib, rating, star, street, district, city, province, description)
        VALUES (%s, %s, %s, %s, 0, 1, %s, %s, %s, %s, 'hotel');
    """
    data = (email, password, owner_first_name, owner_last_name, email, owner_phone_number,
            email, hotel_name, hotel_branch, business_license, street_name, district, city, province)


    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()
