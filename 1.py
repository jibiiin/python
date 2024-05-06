file=open("data.txt","w")
select=int(input("select a number(1 Add, 2 Select, 3 Edit, 4 Delete)"))
def add():
    if select==1:
        n=input("enter a name:")
        file.write(n+"\n")
        print(n+" Added successfully")
        add()
    elif select==2:
        file=open("data.txt","r")
        content=file.read()
        n=input("enter a selected id: ")
        if n in content:
            print("Your Selected :"+n)
        else:
            print("Name not found")
        file.write(n+"\n")
        print(n+" selected succesfully")
    elif select==4:
        file.open("data.txt","r")    
