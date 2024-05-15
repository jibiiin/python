import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
name=input("enter a name :")
if conn:
    cur.execute("DELETE FROM shadow WHERE NAME='%s'"%name)
    conn.commit()
    print("%s deleted success"%name)
else:
    print("connection failed")    