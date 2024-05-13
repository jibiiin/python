import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
if conn:
    cur.execute("insert into jiji value('anu',20,30)")
    conn.commit()
    print("Insert data created success")
else:
    print("connection failed")    