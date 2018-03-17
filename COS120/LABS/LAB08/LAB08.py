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
        drawSquare(t,x,y,size,"#990000")
        x=x+size

def drawRedBlackRow(t,x,y,size):
    for i in range(4):
        drawSquare(t,x,y,size,"#990000")
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
    
def showBoard(CB):
    alpha="ABCDEFGH"
    j=0
    print("   0  1  2  3  4  5  6  7")
    for i in alpha:
        print(i,CB[j])
        j+=1
        
def CBAdjuster(row,column,color,CB):
    alpha="ABCDEFGH"
    j=0
    if color=="red":
        CB[row][column]=1
    else:
        CB[row][column]=3
    return CB

def drawChecker(t,row,column,color,size,CB):
    t.color("black",color)
    t.up()
    y=rowToLocation(row, size)-(size//2)
    x=colToLocation(column,size)+(size//2)
    t.goto(x,y)
    CBAdjuster(row,column,color,CB)
    t.down()
    t.begin_fill()
    ps=t.pensize()
    t.pensize(2)
    drawCircleCentered(t,size//2)
    t.end_fill()
    drawCircleCentered(t,size//3)
    drawCircleCentered(t,size//6)
    t.pensize(ps)
    return CB
        
def fillCheckerBoard(t,size,CB):
    for row in range(3):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"red",size,CB)
    for row in range(5,8,1):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"gray",size,CB)
    return CB

def moveChecker(t,size,move,color,CB):
    alpha="ABCDEFGH"
    j=0
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
    if CB[fromRow][fromCol]==1:
        drawChecker(t,toRow,toCol,"red",size,CB)
    else:
        drawChecker(t,toRow,toCol,"gray",size,CB)
    CB[fromRow][fromCol]=0
    #draw the checker
##    drawChecker(t,toRow,toCol,color,size,CB)
    showBoard(CB)
    return CB
    
def checkers(size):
    alpha="ABCDEFGH"
    j=0
    CB=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    sue=cTurtle.Turtle()
    sue.tracer(False)  
    drawCheckerBoard(sue,-4*size,4*size,size)
    labelBoard(sue,size)
    fillCheckerBoard(sue,size,CB)
    sue.tracer(True)
    showBoard(CB)
    for i in range(200):
        redMove=input("Enter gray checker move=> ")
        if redMove=="exit":
            return
        else:
            moveChecker(sue,size,redMove,"red",CB)
        grayMove=input("Enter red checker move=> ")
        if grayMove=="exit":
            return
        else:
            moveChecker(sue,size,grayMove,"gray",CB)
    sue.exitOnClick()

checkers(60)
