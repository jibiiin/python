class Student:
    def data(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def total(self):
        self.z=self.a+self.b+self.c+self.d      
        print("total mark :",self.z)
    def percentage(self):
        self.x=self.z*100//400    
        print("percentage mark",self.x)
    def average(self):
        self.y=self.z//4
        print("average mark :",self.y)    
        
x=Student()
x.data(1,2,3,4)
x.total()
x.percentage()
x.average()
