#Found & Correct Place +1 cow
#Found & Wrong Place +1 bull
secret_number="1038"
#number=int(input("Enter your guess: "))
cows=bulls=Track=0
while(cows!=4):
    number=input("Enter your guess: ")
    Track+=1
    if(number == secret_number):
        cows=4
    else:
        cows=bulls=0
        for x in range(4):
            if(secret_number.count(number[x])==1): #if found
                if (secret_number[x]!=number[x]): #if not at the same position
                    bulls+=1
                else: #if at the same position
                    cows+=1
        print("You have ",cows," cows and ",bulls," bulls")
print("\n\nNumber of guesses: ",Track)
input("GAME OVER")