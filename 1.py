def add():
    file=open("data.txt","a")
    select=int(input("select a number(1 Add, 2 Select, 3 Edit, 4 Delete)"))
    if select==1:
        n=input("enter a name:")
        file.write(n+"\n")
        print(n+" Added successfully")
        file.close()
        add()
    elif select==2:
        file1=open("data.txt","r")
        content=file1.read()
        n=input("enter a selected name: ")
        if n in content:
            print("Your Selected :"+n)
        else:
            print("Name not found")
        file.write(n+"\n")
        print(n+" selected succesfully")        
        add()
    elif select==4:
        file1.open("data.txt","r")    
        name=input("enter a name:")
        content=file1.read()
        if name in content:
            li=list(content.split("\n"))
            data=li.index(name)
            del li[data]
            str1="\n"    
            newdata=str1.join(li)
            file1=open("data.txt","w")
            file1.write(newdata) 
            print(name + "Deleted succesfully")
            add()
        else:
            print("No")
add()