from tkinter import*
window=Tk()
window.title("welcome")
window.geometry("220x300")
window.resizable(False,False)
window.configure(background="#50252d")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
e1=Entry()
e1.place(x=50,y=20)
btn1=Button(text=" 1")
btn1.place(x=10,y=50)
btn2=Button(text=" 4")
btn2.place(x=30,y=50)
btn3=Button(text="3 ")
btn3.place(x=10,y=100)
btn4=Button(text=" 6 ")
btn4.place(x=30,y=100)
btn5=Button(text=" 7 ")
btn5.place(x=50,y=50)
btn6=Button(text=" 2 ")
btn6.place(x=10,y=75)
btn7=Button(text=" 5 ")
btn7.place(x=30,y=75)
btn8=Button(text=" 8 ")
btn8.place(x=50,y=75)
btn9=Button(text=" 9 ")
btn9.place(x=50,y=100)
btn10=Button(text=" 0 ")
btn10.place(x=30,y=125)
btn11=Button(text=" - ")
btn11.place(x=10,y=125)
btn12=Button(text="+")
btn12.place(x=70,y=50)
btn13=Button(text=" * ")
btn13.place(x=50,y=125)
btn14=Button(text=" /")
btn14.place(x=70,y=75)
btn15=Button(text="=")
btn15.place(x=70,y=100)
btn16=Button(text="%")
btn16.place(x=70,y=125)
window.mainloop()