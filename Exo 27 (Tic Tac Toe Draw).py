def Play1_move(game,move):
    coords=move.split(",")
    x=int(coords[0])-1
    y=int(coords[1])-1
    if(game[x][y]!=0):print("**Position already full.Enter a new position");return False
    game[x][y]='O'
    return True
    
def Play2_move(game,move):
    coords=move.split(",")
    x=int(coords[0])-1
    y=int(coords[1])-1
    if(game[x][y]!=0):print("**Position already full.Enter a new position");return False
    game[x][y]='X'
    return True

def show(game):
    print(game[0])
    print(game[1])
    print(game[2])

def main():
	Squares_available=len(game)*len(game[0])
	p=1
	while(Squares_available !=0):
		if(p==1):
			ok=False
			while(not ok):
				Player1_move=input("\n\nPlayer1 What's your move? ")
				ok=Play1_move(game,Player1_move)
			p=2
			Squares_available-=1
			show(game)
        
		else:
			ok=False
			while(not ok):
				Player2_move=input("\n\nPlayer2 What's your move? ")
				ok=Play2_move(game,Player2_move)
			p=1
			Squares_available-=1
			show(game)
	input("\n\nGAME OVER")
if __name__=="__main__":
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]
	main()