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



def main():
	print(check_STRIKE_line_by_line(game))
	print(check_STRIKE_Column_by_Column(game))
	print(check_STRIKE_by_diagonal(game))

if __name__=="__main__":
	game = [[0, 1, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
	main()