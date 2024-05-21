import mysql.connector
from tkinter import *
import tkinter.messagebox as message
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="file")
cur=conn.cursor()
def save():
    n=name.get()
    a=address.get()
    p=phone.get()
if conn:
    window=Tk()
    window.title("welcome")
    window.geometry("220x300")
    window.resizable(False,False)
    window.configure(background="#50252d")
    window.attributes("-topmost",True)
    window.attributes("-alpha",0.9)
    window.iconbitmap("favicon.ico")
    lbl1=Label(text=" name:-  ")
    lbl1.place(x=20,y=30)
    lbl2=Label(text="address:-")
    lbl2.place(x=20,y=50)
    lbl3=Label(text=" phone:- ")
    lbl3.place(x=20,y=70)
    e1=Entry()
    e1.place(x=80,y=30)
    e2=Entry()
    e2.place(x=80,y=50)
    e3=Entry()
    e3.place(x=80,y=70)
    btn=Button(text="  save  ",command="save")
    btn.place(x=85,y=100)
else:
    print("connection failed")

window.mainloop()  
 
