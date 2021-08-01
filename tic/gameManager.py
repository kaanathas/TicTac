
from tic import data as data
from tic import board as bd
from tic import htmlGen
import restoreDb
exit=False
winner=None
currentPlayer="X"
bd.board
player1=None
player2=None
winPlayer=0

def playerName():
    global player1 
    global player2
    player1=input("Enter Player1 Name, for \"X\" \n")
    player2=input("Enter Player2 Name, for \"O\" \n")

def updateDatabase(player1,player2,winPlayer):
    data.insertData(player1,player2,winPlayer)

def displayMenu():
    print("\nE = Exit   H= status\n")

def showHistory():
    history=data.history()
    print("------------------plays summary----")
    print("TOTAL PLAYS         =>"+str(history["total"]))
    print("TOTAL PLAYER 1 WINS =>"+str(history[1]))
    print("TOTAL PLAYER 2 WINS =>"+str(history[2]))
    print("TOTAL TIES          =>" +str(history[0]))
    print("-----------------------------------")
    key=input("\n 1. ENTER b TO GO BACK \n 2. ENTER h TO SEE FULL HISTORY ON BROWSER\n")
    if key=="b":
        return
    if key=="h":
        htmlGen.htmlPage()
        showHistory()
        
def Turn(currentPlayer):
    global exit
    if currentPlayer=="X":
        print("\n"+player1 +" s turn ")
    else:
        print("\n"+player2 +" s turn")
    displayMenu()
    keyboardKey=None
    valid=False
    while not valid:
        keyboardKey=input("To Choose a position 1-9\n")
        while keyboardKey  not in ["1","2","3","4","5","6","7","8","9","E" ,"H"]:
            keyboardKey=input("To play please choose a position 1-9\n")
        if keyboardKey=="E":
            exit=True
            return
        elif keyboardKey=="H":
            showHistory()
            bd.displayBoard()
        else:
            keyboardKey=int(keyboardKey)-1
            if bd.board[keyboardKey]=="-":
                valid=True
            else:
                print("you can't choose it, try again")
    bd.board[keyboardKey]=currentPlayer
    bd.displayBoard()
    
def changePlayer():
    global currentPlayer
    if not exit:
        if currentPlayer=="X":
            currentPlayer="O"
        elif currentPlayer=="O":
            currentPlayer="X"
    return

def playGame():
    global player1
    global player2
    global winPlayer
    
    playerName()
    while not exit:
        bd.board=[
       "-","-","-",
       "-","-","-",
       "-","-","-",
       ]
        bd.playing=True
        bd.displayBoard()
        winner=None
        while bd.playing:

            Turn(currentPlayer)

            winner=bd.GameOver()

            changePlayer()
            if exit:
                bd.playing=False
        if not exit:
            if winner=="X" or winner=="O":
                if winner=="X":
                    winPlayer=1
                    print("\n"+player1 +"  WON")
                else:
                    winPlayer=2
                    print("\n"+player2 +"  WON")
                
            elif winner==None:
                print("\n Tie")
            updateDatabase(player1,player2,winPlayer)
            END="""
  _____  _           __     __           _____          _____ _   _ 
 |  __ \| |        /\\\\ \   / /     /\   / ____|   /\   |_   _| \ | |
 | |__) | |       /  \\\\ \_/ /     /  \ | |  __   /  \    | | |  \| |
 |  ___/| |      / /\ \\\\   /     / /\ \| | |_ | / /\ \   | | | . ` |
 | |    | |____ / ____ \| |     / ____ \ |__| |/ ____ \ _| |_| |\  |
 |_|    |______/_/    \_\_|    /_/    \_\_____/_/    \_\_____|_| \_|
                                                                    
....... 
"""
            print(" \n"+END+"\n")
            
    return
    
def gameManeger():
        restoreDb.importDb()
        playGame()


