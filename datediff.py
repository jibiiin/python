from datetime import date
starting_date=date(2000,1,1)
ending_date=date(2024,1,1)
nod=(ending_date-starting_date).days
years=nod//365
leapyears=years//4
print(years)
print(leapyears)


