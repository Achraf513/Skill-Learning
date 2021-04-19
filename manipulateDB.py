import sqlite3 as sql
from Classes.Student import *
from Classes.Payment import *
from Classes.Teacher import *

def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file) 
        return conn
    except sql.Error as e: 
        print("an error has occurred")
        return conn


def create_table(conn, create_table_sql):
    try:
        curs = conn.cursor()
        curs.execute(create_table_sql)
        conn.commit()
    except sql.Error as e:
        print(e)


def crud(conn, crud, sqlite_query):
    # crud = c >> create/insert
    # crud = r >> read/select
    # crud = u >> update
    # crud = d >> delete
    try:
        curs = conn.cursor()
        curs.execute(sqlite_query)
        conn.commit()
        if(crud=='r'):
           rows = curs.fetchall() 
           return rows
        elif(crud=='c'):
            return curs.lastrowid
        else: 
            return None
    except sql.Error as error:
        print("Failed to insert data into sqlite table", error)
    
        
conn = create_connection("database.db")
 
create_table(conn, Student.sql_create_student_table) 
create_table(conn, Payment.sql_create_payment_table) 
create_table(conn, Teacher.sql_create_teacher_table) 