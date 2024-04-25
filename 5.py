name=[]
def start():
    select=int(input("Select a number(1 Add, 2 Select, 3 Edit, 4 Delete , 5 Exit)"))
    if select==1:
        n=input("enter a name :")
        name.append(n)
        print(name)
        start()
    elif select==2:
        n=input("Enter a selected name :")
        if n in name:
            print(n)
        else:
            name.append(n)
            print(name)    
        data=name.index(n)
        print("your selected name :",name[data])
        start()
    elif select==3:
        n=input("enter a anme")
        m=input("replaced name")
        if n in name:
             data=name.index(n)
             name[data]=m
             print(name)
        else:
            print("n is not in  the list",n)    
        start()    
    elif select==4:
        n=input("enter a name")
        data=name.index(n)
        del name[data]
        print(name)
        start()
    else:
        exit()        
start()        