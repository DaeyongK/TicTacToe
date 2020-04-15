game = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]
#Project Idea; player will enter a number on the board, and the corresponding
#board space will turn to that player's number
goodSpot = False
gameOn = True
fill = 0
def gridCheck(game, p1Vic, p2Vic):
    #rows
    p1Vic = False
    p2Vic = False
    for x in range(0,3):
        rowSet = set([game[x][0], game[x][1], game[x][2]])
        if len(rowSet) == 1 and game[x][0] != " ":
            if rowSet == {"o"}:
                print("Player 1 wins horizontally!")
                p1Vic = True
                return p1Vic
                break
            else:
                print("Player 2 wins horizontally!")
                p2Vic = True
                return p2Vic
                break
    #columns
    for x in range(0,3):
        columnSet = set([game[0][x], game[1][x], game[2][x]])
        if len(columnSet) == 1 and game[0][x] != " ":
            if columnSet == {"o"}:
                print("Player 1 wins vertically!")
                p1Vic = True
                return p1Vic
                break
            else:
                print("Player 2 wins vertically!")
                p2Vic = True
                return p2Vic
                break
    #diagonals
    diagonal1 = set([game[0][0], game[1][1], game[2][2]])
    diagonal2 = set([game[0][2], game[1][1], game[2][0]])
    if len(diagonal1) == 1 or len(diagonal2) == 1 and game[1][1] != " ":
        if diagonal1 == {"o"} or diagonal2 == {"o"}:
            print("Player 1 wins diagonally!")
            p1Vic = True
            return p1Vic
        elif diagonal1 == {"x"} or diagonal2 == {"x"}:
            print("Player 2 wins diagonally!")
            p2Vic = True
            return p2Vic
        
def setBoard(game):
    print(" "+game[0][0]+" | "+game[0][1] , "| "+game[0][2])
    print("-----------")
    print(" "+game[1][0]+" | "+game[1][1] , "| "+game[1][2])
    print("-----------")
    print(" "+game[2][0]+" | "+game[2][1] , "| "+game[2][2])

def p1Run(goodSpot, game):
    while goodSpot == False:
        row = input("P1: Which row? Row: ")
        column = input("P1: Which column? Column: ")
        goodSpot = False
        try:
            Row = int(row) - 1
            Column = int(column) - 1
            if game[Row][Column] == "o" or game[Row][Column] == "x":
                print("Spot unavailable")
                continue
            else:
                game[Row][Column] = "o"
                goodSpot = True
        except:
            print("Spot unavailable")
            continue

def p2Run(goodSpot, game):
    while goodSpot == False:
        row = input("P2: Which row? Row: ")
        column = input("P2: Which column? Column: ")
        goodSpot = False
        try:
            Row = int(row) - 1
            Column = int(column) - 1
            if game[Row][Column] == "o" or game[Row][Column] == "x":
                print("Spot unavailable")
                continue
            else:
                game[Row][Column] = "x"
                goodSpot = True
        except:
            print("Spot unavailable")
            continue
            
setBoard(game)  
while fill < 9:
    if fill < 9:
        p1Vic = False
        p2Vic = False
        p1Run(goodSpot, game)
        setBoard(game)
        p1Vic = gridCheck(game, p1Vic, p2Vic)
        if p1Vic == True:
            break
        fill = fill + 1
    if fill < 9:
        p1Vic = False
        p2Vic = False
        p2Run(goodSpot, game)
        setBoard(game)
        p2Vic = gridCheck(game, p1Vic, p2Vic)
        if p2Vic == True:
            break
        fill = fill + 1
    if fill == 9:
        print("Tie!")      
