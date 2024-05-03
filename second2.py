file=open("text123.txt","a")
def add():
    name=input("enter your name")
    address=input("enter your address")
    phone=input("enter phone number")
    file.write("name:"+name+"\naddress :"+address+"\nphone:"+phone+"\n_____________\n")
    print(name+ "details added succesfully")
for a in range(3):
    add() 


