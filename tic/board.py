board=[]
playing=False

def displayBoard():
    # print("  "+"_"+"   "+"_"+"   "+"_"+"  ")
    print("\n| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
    # print("| "+"_"+" | "+"_"+" | "+"_"+" |")

def Row():
    global playing
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    
    if row1 or row2 or row3:
        playing=False
        if row1:
            return board[0]
        if row2:
            return board[3]
        if row3:
            return board[6]
    
    return

def Coloums():
    global playing
    col1=board[0]==board[3]==board[6]!="-"
    col2=board[1]==board[4]==board[7]!="-"
    col3=board[2]==board[5]==board[8]!="-"

    if col1 or col2 or col3:
        playing=False
        if col1:
            return board[0]
        if col2:
            return board[1]
        if col3:
            return board[2]
    
    
    return

def Diagonal():
    global playing
    dia1=board[0]==board[4]==board[8]!="-"
    dia2=board[2]==board[4]==board[6]!="-"
    

    if dia1 or dia2:
        playing=False
        if dia1:
            return board[0]
        if dia2:
            return board[2]
    
    return

def GameOver():
    Tie()
    return Win()
    
def Win():
    
    # chech row , coloum ,dia
    rowWinner=Row()
    coloumWinner=Coloums()
    diagonalWinner=Diagonal()

    if rowWinner:
        winPlayer=rowWinner
    elif coloumWinner:
        winPlayer=coloumWinner

    elif diagonalWinner:
        winPlayer=diagonalWinner
    else:
        winPlayer=None

    return winPlayer

def Tie():
    global playing
    if "-" not in board:
        playing=False
    return
