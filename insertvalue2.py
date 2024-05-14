import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="mysql")
cur=conn.cursor()
mark=[20,30,40]
select=int(input("select a number(1 add,2 select,3 edit,4 delete)"))
if select==1:
    n=input("enter a mark: ")
    name.append()
    print(mark)
elif select==2:
    n=input("enter a selected name :")
    print(n)

