from collections import Counter

def Get_Month_by(number):
    Months={"January":1, "February":2,"Mars":3, "Avril":4, "May":5, 
            "June":6, "July":7, "August":8, "September":9, "November":10,
            "December":12}
    for x in Months:
        if(Months.get(x)==number):
            return x

Birthdates={"Albert Einstein":[3,14,1879],
            "Benjamin Franklin":[1,17,1700], 
            "Ada Lovelace":[12,10,1815],
            "Hamza Saber":[5,17,1997],
            "Stangel":[12,12,1996]
            }


birthday_Months=[Get_Month_by((Birthdates.get(x))[0]) for x in Birthdates]
c=Counter(birthday_Months)
for x in c:
    print("There are",c[x],"birthdays in",x)