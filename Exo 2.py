number=int(input("Enter a number: "))

if(number & 1):
	print(str(number)+" is Odd")
else:
	print("%d is %s"% (number,"Even"))

if(number%4==0):
	print(str(number)+" is multiple of 4")

num=int(input("Enter a number you want to check: "))
check=int(input("Enter a number of checking: "))
if(num%check==0):print(str(check)+" divides evenly "+str(num))
else:print(str(check)+" doesn't divides evenly "+str(num))