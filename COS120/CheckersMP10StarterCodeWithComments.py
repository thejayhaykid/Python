import cTurtle
import math
import random

def drawSquare(t,x,y,size,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def drawBlackRedRow(t,x,y,size):
    for i in range(4):
        drawSquare(t,x,y,size,"black")
        x=x+size
        drawSquare(t,x,y,size,"#009900")
        x=x+size

def drawRedBlackRow(t,x,y,size):
    for i in range(4):
        drawSquare(t,x,y,size,"#009900")
        x=x+size
        drawSquare(t,x,y,size,"black")
        x=x+size

def drawCheckerBoard(t,x,y,size):
    for i in range(4):
        drawRedBlackRow(t,x,y,size)
        y=y-size
        drawBlackRedRow(t,x,y,size)
        y=y-size
        
def labelBoard(t,size):
    t.up()
    t.goto(-(4*size)+8,(4.05*size))
    t.down()
    t.pencolor('#000000')
    for i in range(8):
        t.write("COL " + str(i),font=("Arial",12,"bold"))
        t.up()
        t.forward(size)
        t.down()
    t.up()
    t.goto(-(5.2*size),(3.4*size))
    t.down()
    for i in range(8):
        t.write("ROW " + chr(65+i),font=("Arial",12,"bold"))
        t.up()
        t.goto(-(5.2*size),((4*size)+(i*-size)-(1.7*size)))
        t.down()
        
def rowToLocation(row,size):
    return (4*size)-(size*row)

def colToLocation(col,size):
    return -(4*size)+(size*col)

def drawCircleCentered(t,radius):
    pos=t.position()
    t.up()
    t.forward(radius)
    t.down()
    t.lt(90)
    t.circle(radius)
    t.up()
    t.setpos(pos)
    t.down()

def drawChecker(t,row,column,color,size):
    t.color("black",color)
    t.up()
    y=rowToLocation(row, size)-(size//2)
    x=colToLocation(column,size)+(size//2)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    ps=t.pensize()
    t.pensize(2)
    drawCircleCentered(t,size//2)
    t.end_fill()
    drawCircleCentered(t,size//3)
    drawCircleCentered(t,size//6)
    t.pensize(ps)
        
def fillCheckerBoard(t,size,CB):
    for row in range(3):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"red",size)
            CB[row][col]=1
    for row in range(5,8,1):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"gray",size)
            CB[row][col]=3

def moveChecker(t,size,move,color,CB):
    #parse the move
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    #get graphic x,y from row,col
    y=rowToLocation(fromRow, size)
    x=colToLocation(fromCol, size)
    #blank out the from square
    drawSquare(t,x,y,size,"black")
    #draw the checker
    drawChecker(t,toRow,toCol,color,size)
    #move the checker in the actual board
    CB[toRow][toCol]=CB[fromRow][fromCol]
    CB[fromRow][fromCol]=0
    

def showBoard(CB):
    print("  0 1 2 3 4 5 6 7 ")
    for row in range(8):
        line=chr(row+65)+" "
        for col in range(8):
            line+=str(CB[row][col])+" "
        print(line)

def isNotValidMove(move,CB,player):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    #FOR BOTH RED AND BLACK
    #Check for valid range for rows and columns (on board)
    #Check for only +1 or -1 in column change (since no jumps yet)
    if CB[toRow][toCol] != 0: #Can not move to a non-empty square
        print("Occupied")
        return True
    if (toRow+toCol)%2 != 1: #Can not move to a non-black square
        print("Must move to black square")
        return True
    
    #CHECK BY COLORS
    if player == "gray":
        #check for gray checker to be moved
        if CB[fromRow][fromCol] not in [3,4]:
            print("You cannot move your opponent!")
            return True
        #check new row is 1 less than old row (unless a king...)
        
    else: #red
        #check for red checker to be moved
        if CB[fromRow][fromCol] not in [1,2]:
            print("You cannot move your opponent!")
            return True
        #check new row is 1 greater than old row (unless a king...)
        
    return False
    
def checkers(size):
    CB=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    sue=cTurtle.Turtle()
    sue.tracer(False)  
    drawCheckerBoard(sue,-4*size,4*size,size)
    labelBoard(sue,size)
    fillCheckerBoard(sue,size,CB)
    sue.tracer(True)
    for i in range(1000):
        player="gray"
        move=input("Enter gray checker move => ")
        while isNotValidMove(move,CB,player):
            move=input("Enter gray checker move => ")
            if  move=="exit":
                return
        moveChecker(sue,size,move,"gray",CB)
        showBoard(CB)
            
        player="red"
        move=input("Enter red checker move => ")
        while isNotValidMove(move,CB,player):
            move=input("Enter red checker move => ")
            if  move=="exit":
                return
        moveChecker(sue,size,move,"red",CB)
        showBoard(CB)


checkers(60)
