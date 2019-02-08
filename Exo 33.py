Birthdates={"Albert Einstein":"3/14/1879",
            "Benjamin Franklin":"01/17/1706", 
            "Ada Lovelace":"12/10/1815"
            }
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for item in Birthdates:
    print(item)

person=input("Who's birthday do you want to look up?")

if(person in Birthdates):
    print("%s's birthday is %s"%(person,Birthdates.get(person)))
else:
    print("The person can't be found")
