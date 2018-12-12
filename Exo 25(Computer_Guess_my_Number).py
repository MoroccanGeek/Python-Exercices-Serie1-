import random
number=90
answer=""
x=1
y=100
track=0
while(answer!="yes"):
    track+=1
    guess=random.randint(x,y)
    print(guess,end=" ")
    answer=input("is this ur number?: ")
    if(answer=="low"):
        y=guess-1
    elif(answer=="high"):
        x=guess+1
print("Phew, Finally dude after ",track," guesses i've finally found it")