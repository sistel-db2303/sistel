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



########## INSERT SQL HERE#################     
INSERT INTO SHUTTLE_SERVICE VALUES 
(81234567890,'B 1234 AB'),
	(82123456789,'D 5678 CD'),
	(83876543210,'J 2345 JK'),
	(85643210987,'F 9012 EF'),
	(81367890123,'G 3456 FG');

""")


# commit the changes
conn.commit()
print("Task finished successfully")


