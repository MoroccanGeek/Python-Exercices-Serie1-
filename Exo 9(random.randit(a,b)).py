import random
track=0
Random_number=random.randint(1,9)
while(1):
	guess=input("Guess the number: ")
	if(guess=="exit"): break
	if(int(guess)<Random_number):
		print("you've guessed very low")
	elif(int(guess)>Random_number):
		print("you've guessed very high")
	else:
		track+=1
		break
	track+=1
print()
print("You've guessed exactly right, you're number of guesses is: ",track)
input("GAME OVER")