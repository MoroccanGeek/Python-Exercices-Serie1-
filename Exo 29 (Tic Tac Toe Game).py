def Draw_Board(g):
    
    for x in range(len(g)):
        print(" --- "*len(g))
        for y in range(len(g)):
            if(g[x][y]==0):
                if(y==2):
                    print("|   |")
                else:
                    print("|   |",end="")
            elif(g[x][y]==1):
                if(y==2):
                    print("| X |")
                else:
                    print("| X |",end="")
            else:
                if(y==2):
                    print("| O |")
                else:
                    print("| O |",end="")
    print(" --- "*len(g))

#From Exo26
def check_STRIKE_line_by_line(game):
    
    for i in game:
        if all(i) and (i.count(1)==3 or i.count(2)==3):
            return True
    return False

def check_STRIKE_Column_by_Column(game):
    tempo=[]
    
    for j in range(len(game)):
        for i in game:
            tempo.append(i[j])
        if all(tempo) and (tempo.count(1)==3 or tempo.count(2)==3):
            return True
        else:
            tempo.clear()
    return False

def check_STRIKE_by_diagonal(game):
    diagonal1=[]
    diagonal2=[]
    
    for j in range(len(game)):
        diagonal1.append(game[j][j])
        diagonal2.append(game[j][len(game)-1-j])
    if (diagonal1.count(1)==3 or diagonal1.count(2)==3) or (diagonal2.count(1)==3 or diagonal2.count(2)==3):
        return True
    return False

#From Exo27	
def Play1_move(game,move):
    coords=move.split(",")
    x=int(coords[0])-1
    y=int(coords[1])-1
    if(game[x][y]!=0):print("**Position already full.Enter a new position");return False
    game[x][y]=1
    return True
    
def Play2_move(game,move):
    coords=move.split(",")
    x=int(coords[0])-1
    y=int(coords[1])-1
    if(game[x][y]!=0):print("**Position already full.Enter a new position");return False
    game[x][y]=2
    return True

def main():
	Squares_available=len(game)*len(game[0])
	p=1
	winner=0
	while(Squares_available !=0):
		if(p==1):
			ok=False
			while(not ok):
				Player1_move=input("\n\nPlayer1 What's your move? ")
				ok=Play1_move(game,Player1_move)
			p=2
			Squares_available-=1
			Draw_Board(game)
			if(check_STRIKE_line_by_line(game) or check_STRIKE_Column_by_Column(game) or check_STRIKE_by_diagonal(game)):
				Winner=1
				break;
        
		else:
			ok=False
			while(not ok):
				Player2_move=input("\n\nPlayer2 What's your move? ")
				ok=Play2_move(game,Player2_move)
			p=1
			Squares_available-=1
			Draw_Board(game)
			if(check_STRIKE_line_by_line(game) or check_STRIKE_Column_by_Column(game) or check_STRIKE_by_diagonal(game)):
				Winner=2
				break
	if(Squares_available==0):
		print("All is FULL")
	else:
		print("Winner is Player: ",Winner)
	input("\n\nGAME OVER.")
	
if __name__=="__main__":
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]
	main()