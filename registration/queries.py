import psycopg2
from django.shortcuts import render, redirect


DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'bGfD-1fc22D*4fDEC4-d331f-25c6bbe'
DB_HOST = 'monorail.proxy.rlwy.net'
DB_PORT = '59422'

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
        INSERT INTO Customer (email, password, first_name, last_name, phone_number, nik)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (email, password, first_name, last_name, phone_number, nik)

    try:
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()
        return redirect('/login.html')
    except psycopg2.Error as e:
        connection.rollback()
        print("Gagal menyimpan data Customer:", e)
        return render(request, 'registration.html', {'error_message': 'Gagal register data. Silakan coba lagi.'})

def insert_hotel(email, password, owner_first_name, owner_last_name, owner_phone_number,
                 business_license, hotel_name, hotel_branch, street_name, district, city, province):
    connection = initialize_connection()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO Hotel (email, password, owner_first_name, owner_last_name, owner_phone_number,
                           business_license, hotel_name, hotel_branch, street_name, district, city, province)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (email, password, owner_first_name, owner_last_name, owner_phone_number,
            business_license, hotel_name, hotel_branch, street_name, district, city, province)

    try:
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()
        return redirect('/login.html')
    except psycopg2.Error as e:
        connection.rollback()
        print("Gagal menyimpan data Hotel:", e)
        return render(request, 'registration.html', {'error_message': 'Gagal register data. Silakan coba lagi.'})
