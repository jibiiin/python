class first:
    def one(self):
        print("It is a first class ")

class second:
    def two(self):        
        print("it is the second class")

class third(first,second):
    def three(self):
        print("it is the third class")

x=third()
x.one()
x.two()
x.three()
