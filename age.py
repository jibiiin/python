#from datetime import date
#start_date=date(2024,5,1)
#today=date.today()
#nod=(today-start_date).days()
#print(nod)

from datetime import date
birth_date=date(2003,7,7)
today=date.today()
nod=(today-birth_date).days
age=nod//365
print(age)