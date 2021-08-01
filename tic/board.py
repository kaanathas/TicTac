board=[]
gameStill=False

def displayBoard():
    # print("  "+"_"+"   "+"_"+"   "+"_"+"  ")
    print("\n| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")

def checkRow():
    global gameStill
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    
    if row1 or row2 or row3:
        gameStill=False
        if row1:
            return board[0]
        if row2:
            return board[3]
        if row3:
            return board[6]
    
    return

def checkColoums():
    global gameStill
    col1=board[0]==board[3]==board[6]!="-"
    col2=board[1]==board[4]==board[7]!="-"
    col3=board[2]==board[5]==board[8]!="-"

    if col1 or col2 or col3:
        gameStill=False
        if col1:
            return board[0]
        if col2:
            return board[1]
        if col3:
            return board[2]
    
    
    return

def checkDiagonal():
    global gameStill
    dia1=board[0]==board[4]==board[8]!="-"
    dia2=board[2]==board[4]==board[6]!="-"
    

    if dia1 or dia2:
        gameStill=False
        if dia1:
            return board[0]
        if dia2:
            return board[2]
    
    return

def checkGameOver():
    checkTie()
    return checkWin()
    
def checkWin():
    
    # chech row , coloum ,dia
    rowWinner=checkRow()
    coloumWinner=checkColoums()
    diagonalWinner=checkDiagonal()

    if rowWinner:
        winPlayer=rowWinner
    elif coloumWinner:
        winPlayer=coloumWinner

    elif diagonalWinner:
        winPlayer=diagonalWinner
    else:
        winPlayer=None

    return winPlayer

def checkTie():
    global gameStill
    if "-" not in board:
        gameStill=False
    return
