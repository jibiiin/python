import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="")
cur=conn.cursor()
if conn:
    cur.execute("CREATE DATABASE HELLO2")
    print("Database created")
else:
    print("connection failed")    