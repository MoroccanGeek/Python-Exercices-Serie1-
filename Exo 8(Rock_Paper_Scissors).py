while(1):
    Answer=input("Do you wanna play?: ")
    if(Answer=="yes"):
        player1_move=input("Enter your move: ")
        player2_move=input("Enter your move: ")
        if(player1_move==player2_move):
            print("It's a tie")
        else:
            list=[] #list of tuples
            list.append((1,player1_move))
            list.append((2,player2_move))
            
	    #This will convert our list of Tuples into dictionaries where keys are item[0] of tuple 
	    #and values are item[1] of tuple
	    dicdoc=dict(list) 
            
	    if(dicdoc.get(1) in "PaperRock" and dicdoc.get(2) in "PaperRock"):
                Winner_ID=[k for k,v in dicdoc.items() if(v=="Paper")]
            elif(dicdoc.get(1) in "RockScissors" and dicdoc.get(2) in "RockScissors"):
                Winner_ID=[k for k,v in dicdoc.items() if(v=="Rock")]
            else:
                Winner_ID=[k for k,v in dicdoc.items() if(v=="Scissors")]
            print("The winner is player number: ",Winner_ID[0],"\n\n")
    else:
        break;
input("Game Over")
