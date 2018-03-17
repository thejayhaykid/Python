import cTurtle
import math
import random

VALID_RANGE=range(8)

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

def drawChecker(t,row,column,color,size,isKing):
    t.tracer(False)
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
    if isKing:
        drawCrown(t,x,y,size)
    t.tracer(True)

def drawCrown(t,x,y,size):
    t.color("yellow","yellow")
    t.up()
    t.goto(x-(.16*size),y-(.24*size))
    t.down()
    t.begin_fill()
    t.setheading(108)
    t.forward(size//3)
    for i in range(5):
        t.right(72)
        t.forward(size//3)
    t.end_fill()    
        
def fillCheckerBoard(t,size,CB):
    for row in range(3):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"red",size,False)
            CB[row][col]=1
    for row in range(5,8,1):
        if row%2==0:
            start=1
        else:
            start=0
        for col in range(start,8,2):
            drawChecker(t,row,col,"gray",size,False)
            CB[row][col]=3

def fillNonStandaradCheckerBoard(t,size,CB):
    counter=0
    for row in CB:
        counter2=0
        for col in row:
            if col==1:
                drawChecker(t,counter,counter2,"red",size,False)
            elif col==2:
                drawChecker(t,counter,counter2,"red",size,True)
            elif col==3:
                drawChecker(t,counter,counter2,"gray",size,False)
            elif col==4:
                drawChecker(t,counter,counter2,"gray",size,True)
            counter2=counter2+1
        counter=counter+1


def moveChecker(t,size,move,color,CB):
    #parse the move
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    #get graphic x,y from row,col
    y=rowToLocation(fromRow, size)
    x=colToLocation(fromCol, size)
    y2=rowToLocation(toRow-1, size)
    x2=colToLocation(toCol-1, size)
    y3=rowToLocation(toRow+1, size)
    x3=colToLocation(toCol+1, size)
    if toRow-1<0:
        y2=rowToLocation(toRow, size)
    if toCol-1<0:
        x2=colToLocation(toCol, size)
    if toRow+1>7:
        y3=rowToLocation(toRow, size)
    if toCol+1>7:
        x3=colToLocation(toCol, size)
    #blank out the from square
    drawSquare(t,x,y,size,"black")
    #move the checker in the actual board
    if CB[fromRow][fromCol] == 3 and fromCol-toCol==2:
        CB[toRow+1][toCol+1]=0
        drawSquare(t,x3,y3,size,"black")
    if CB[fromRow][fromCol] == 3 and fromCol-toCol==-2:
        CB[toRow+1][toCol-1]=0
        drawSquare(t,x2,y3,size,"black")
    if CB[fromRow][fromCol] == 1 and fromCol-toCol==2:
        CB[toRow-1][toCol+1]=0
        drawSquare(t,x3,y2,size,"black")
    if CB[fromRow][fromCol] == 1 and fromCol-toCol==-2:
        CB[toRow-1][toCol-1]=0
        drawSquare(t,x2,y2,size,"black")
    if CB[fromRow][fromCol] == 2 and fromCol-toCol==-2 and fromRow-toRow==-2:
        CB[toRow-1][toCol-1]=0
        drawSquare(t,x2,y2,size,"black")
    if CB[fromRow][fromCol] == 2 and fromCol-toCol==-2 and fromRow-toRow==2:
        CB[toRow+1][toCol-1]=0
        drawSquare(t,x2,y3,size,"black")
    if CB[fromRow][fromCol] == 2 and fromCol-toCol==2 and fromRow-toRow==-2:
        CB[toRow-1][toCol+1]=0
        drawSquare(t,x3,y2,size,"black")
    if CB[fromRow][fromCol] == 2 and fromCol-toCol==2 and fromRow-toRow==2:
        CB[toRow+1][toCol+1]=0
        drawSquare(t,x3,y3,size,"black")
    if CB[fromRow][fromCol] == 4 and fromCol-toCol==-2 and fromRow-toRow==2:
        CB[toRow+1][toCol-1]=0
        drawSquare(t,x2,y3,size,"black")
    if CB[fromRow][fromCol] == 4 and fromCol-toCol==-2 and fromRow-toRow==-2:
        CB[toRow-1][toCol-1]=0
        drawSquare(t,x2,y2,size,"black")
    if CB[fromRow][fromCol] == 4 and fromCol-toCol==2 and fromRow-toRow==-2:
        CB[toRow-1][toCol+1]=0
        drawSquare(t,x3,y2,size,"black")
    if CB[fromRow][fromCol] == 4 and fromCol-toCol==2 and fromRow-toRow==2:
        CB[toRow+1][toCol+1]=0
        drawSquare(t,x3,y3,size,"black")
    if color=="red":
        if toRow != 7:
            CB[toRow][toCol]=CB[fromRow][fromCol]
            CB[fromRow][fromCol]=0
        else:
            CB[toRow][toCol]=2
            CB[fromRow][fromCol]=0
    else: #color is gray
        if toRow != 0:
            CB[toRow][toCol]=CB[fromRow][fromCol]
            CB[fromRow][fromCol]=0
        else:
            CB[toRow][toCol]=4
            CB[fromRow][fromCol]=0
    #draw the checker
    if CB[toRow][toCol] in [2,4]:
        isKing=True
    else:
        isKing=False
    drawChecker(t,toRow,toCol,color,size,isKing)
        
    

def showBoard(CB):
    print("  0 1 2 3 4 5 6 7 ")
    for row in range(8):
        line=chr(row+65)+" "
        for col in range(8):
            line+=str(CB[row][col])+" "
        print(line)

def isNotValidMove(move,CB,player):
    #Parse move into rows and columns
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    fromRow2=fromRow+1
    fromCol2=fromCol+1
    fromRow3=fromRow-1
    fromCol3=fromCol-1
    toRow2=toRow+1
    toCol2=toCol+1
    toRow3=toRow-1
    toCol3=toCol-1
    if fromRow2>7:
        fromRow2=7
    if fromCol2>7:
        fromCol2=7
    if fromRow3<0:
       fromRow3=0 
    if fromCol3<0:
        fromCol3=0
    if toRow2>7:
        toRow2=7
    if toCol2>7:
        toCol2=7
    if toRow3<0:
        toRow3=0
    if toCol3<0:
        toCol3=0
        
    #FOR BOTH RED AND BLACK
    #Check for valid range for rows and columns (on board)
    if fromRow not in VALID_RANGE or fromCol not in VALID_RANGE or toRow not in VALID_RANGE or toCol not in VALID_RANGE:
        print("Row or column specified not in range")
        return True
    #Cannot move empty square
    if CB[fromRow][fromCol] == 0: 
        print("No checker in square")
        return True
    jump = False
    if fromCol-toCol==-2 or fromCol-toCol==2 or fromCol+toCol==-2 or fromCol+toCol==2:
        if CB[fromRow][fromCol]==3:
            if CB[toRow2][toCol3]==1:
                jump = True
            elif CB[toRow2][toCol3]==2:
                jump = True
            elif CB[toRow2][toCol2]==1:
                jump = True
            elif CB[toRow2][toCol2]==2:
                jump = True
        elif CB[fromRow][fromCol]==4:
            if CB[toRow2][toCol2]==1:
                jump = True
            elif CB[toRow2][toCol2]==2:
                jump = True
            elif CB[toRow3][toCol3]==1:
                jump = True
            elif CB[toRow3][toCol3]==2:
                jump = True
            elif CB[toRow2][toCol3]==1:
                jump = True
            elif CB[toRow2][toCol3]==2:
                jump = True
            elif CB[toRow3][toCol2]==1:
                jump = True
            elif CB[toRow3][toCol2]==2:
                jump = True
        elif CB[fromRow][fromCol]==1:
            if CB[toRow3][toCol2]==3:
                jump = True
            elif CB[toRow3][toCol2]==4:
                jump = True
            elif CB[toRow3][toCol3]==3:
                jump = True
            elif  CB[toRow3][toCol3]==4:
                jump = True
        elif CB[fromRow][fromCol]==2:
            if CB[toRow2][toCol2]==3:
                jump = True
            elif CB[toRow2][toCol2]==4:
                jump = True
            elif CB[toRow3][toCol3]==3:
                jump = True
            elif CB[toRow3][toCol3]==4:
                jump = True
            elif CB[toRow2][toCol3]==3:
                jump = True
            elif CB[toRow2][toCol3]==4:
                jump = True
            elif CB[toRow3][toCol2]==3:
                jump = True
            elif CB[toRow3][toCol2]==4:
                jump = True
        else:
            jump = False
    #Check for only +1 or -1 in column change (since no jumps yet)
    if fromCol-toCol not in [-1,1] and jump == False:
        print("Invalid column move")
        return True
    if CB[toRow][toCol] != 0: #Can not move to a non-empty square
        print("Occupied")
        return True
    if (toRow+toCol)%2 != 1: #Can not move to a non-black square
        print("Must move to black square")
        return True
    
    #CHECK BY COLORS
    if player == "gray":  #GRAY CHECKER
        #check for gray checker to be moved
        if CB[fromRow][fromCol] not in [3,4]:
            print("You cannot move your opponent!")
            return True
        #check new row is 1 less than old row (unless a king...)
        if CB[fromRow][fromCol] == 3:
            if fromRow-toRow != 1 and fromRow-toRow != 2:
                print("Attempting to move in wrong direction")
                return True
        else: #is a king
            if fromRow-toRow not in [1,-1,2,-2]:
                print("Invalid row move")
                return True
        
    else: #RED CHECKER
        #check for red checker to be moved
        if CB[fromRow][fromCol] not in [1,2]:
            print("You cannot move your opponent!")
            return True
        #check new row is 1 greater than old row (unless a king...)
        if CB[fromRow][fromCol] == 1:
            if fromRow-toRow != -1 and fromRow-toRow != -2:
                print("Attempting to move in wrong direction")
                return True
        else: #is a king
            if fromRow-toRow not in [1,-1,2,-2]:
                print("Invalid row move")
                return True
        
    return False

def CBString(CB,inputFile):
    readFile = open(inputFile,"r")
    CB=[]
    for aline in readFile:
        CBList=[]
        for achar in aline:
            if achar != '\n':
                CBList.append(int(achar))
        CB.append(CBList)
    readFile.close()
    return CB

def gameOverCheck(CB):
    redcheck=0
    graycheck=0
    for arow in CB:
        for anum in arow:
            if anum==1 or anum==2:
                redcheck+=1
            elif anum==3 or anum==4:
                graycheck+=1
    if graycheck==0 or redcheck==0:
        return True
    else:
        return False
   
def checkers(size):
    CB=[[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [3,0,3,0,3,0,3,0], [0,3,0,3,0,3,0,3], [3,0,3,0,3,0,3,0]]
    sue=cTurtle.Turtle()
    sue.tracer(False)  
    drawCheckerBoard(sue,-4*size,4*size,size)
    labelBoard(sue,size)
    inputFile=input("Enter a file with starting positions you would like => ")
    if inputFile=="":
        fillCheckerBoard(sue,size,CB)
    else:
        CB=CBString(CB,inputFile)
        fillNonStandaradCheckerBoard(sue,size,CB)
    sue.tracer(True)
    gameOverChecker=gameOverCheck(CB)
    counter=0
    player="gray"
    while gameOverChecker==False:
        move=input("Enter "+player+" checker move => ")
        if  move=="exit":
            return
        while isNotValidMove(move,CB,player):
            move=input("Enter "+player+" checker move => ")
            if  move=="exit":
                return
        moveChecker(sue,size,move,player,CB)
        showBoard(CB)
        gameOverChecker=gameOverCheck(CB)
        counter+=1
        if counter%2==0:
            player='gray'
        else:
            player='red'
    print("The game is over!")
    return


checkers(60)
