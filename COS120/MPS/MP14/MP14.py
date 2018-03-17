import cTurtle
import math
import random

EMPTY=0
INCs=[-1,1]
JUMP_INCs=[-2,2]
VALID_RANGE=range(8)
VERBOSE=False
VISIBLE=True

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
    t.tracer(False)  
    for row in VALID_RANGE:
        for col in VALID_RANGE:
            if CB[row][col]!=EMPTY:
                if CB[row][col] in [1,2]:
                    color="red"
                    player="red"
                else:
                    color="gray"
                    player="gray"
                king=False
                if CB[row][col] in [2,4]:
                    king=True
                drawChecker(t,row,col,color,size,king)
    t.tracer(True)
   
def moveChecker(t,size,move,player,CB,possibles):
    if VISIBLE:
        t.tracer(False)  
    if move in possibles["crownings"]:
        row=ord(move[0])-65
        col=int(move[1])
        CB[row][col]+=1
    #in case a multiple jump
    while len(move)>=5:
        fromRow=ord(move[0])-65
        fromCol=int(move[1])
        toRow=ord(move[3])-65
        toCol=int(move[4])
        #get graphic x,y from row,col
        y=rowToLocation(fromRow, size)
        x=colToLocation(fromCol, size)
        #blank out where the checker was
        if VISIBLE:
            drawSquare(t,x,y,size,"black")
        #change the logical board
        temp=CB[fromRow][fromCol]
        CB[fromRow][fromCol]=0                
        CB[toRow][toCol]=temp
        #is this a king?
        king=False
        if temp in[2,4]:
            king=True
        if VISIBLE:
            if player=="gray":
                drawChecker(t,toRow,toCol,"gray",size,king)
            else:
                drawChecker(t,toRow,toCol,"red",size,king)
        #Was this a jump? Remove the intervening checker
        if math.fabs(fromRow-toRow)>1:
            tweenRow=(fromRow+toRow)//2
            tweenCol=(fromCol+toCol)//2
            CB[tweenRow][tweenCol]=0
            y=rowToLocation(tweenRow, size)
            x=colToLocation(tweenCol, size)
            if VISIBLE:
                drawSquare(t,x,y,size,"black")
        move=move[3:]
    t.tracer(True)
      
def showBoard(CB):
    print("  0 1 2 3 4 5 6 7 ")
    for row in range(8):
        line=chr(row+65)+" "
        for col in range(8):
            line+=str(CB[row][col])+" "
        print(line)

def getPossibles(CB,player,VERBOSE):
    possibles={}
    if player=="gray":
        playerTokens=[3,4]
        opponentTokens=[1,2]
        rowInc=-1
        jumpRowInc=-2
    else:
        playerTokens=[1,2]
        opponentTokens=[3,4]
        rowInc=1
        jumpRowInc=2
    possibles["moves"]=findMoves(CB,player,playerTokens,opponentTokens,rowInc)  #puts moves into possibles Dictionary
##    possibles["jumps"]=findJumps(CB,player,playerTokens,opponentTokens,jumpRowInc)
    oldJumps=findJumps(CB,player,playerTokens,opponentTokens,jumpRowInc)
    newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    while newJumps != oldJumps:
        oldJumps=newJumps
        newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    possibles["jumps"]=newJumps
    possibles["crownings"]=findCrownings(CB,player,possibles)
    possibles["blocks"]=findBlocks(CB,player,possibles)
    if VERBOSE:
        print("Moves for "+player+" = ",possibles["moves"])
        print("Jumps for "+player+" = ",possibles["jumps"])
        print("Crownings for "+player+" = ",possibles["crownings"])
        print("Blocks for "+player+" = ",possibles["blocks"])
    return possibles

def validMove(CB,move,player):
    possibles=getPossibles(CB,player,False)
    if len(possibles["jumps"])>0:
        if move not in possibles["jumps"]:
            print("A jump must be taken!!!")
            return False
        else:
            return True
    if move not in possibles["moves"]: #includes crowning and blocking moves
        print ("Invalid move!!!!")
        return False
    else:
        return True 

def findMoves(CB,player,playerTokens,opponentTokens,rowInc):
    moves=[]
    #process all board positions
    for row in VALID_RANGE:
        for col in VALID_RANGE:
            if CB[row][col] in playerTokens:
                if CB[row][col] not in [2,4]: #not a king
                    for colInc in INCs:
                        toRow=row+rowInc
                        toCol=col+colInc
                        if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY:
                            moves.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))
                else: #is a king
                    for rInc in INCs:
                        for colInc in INCs:
                            toRow=row+rInc
                            toCol=col+colInc
                            if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY:
                                moves.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))
    return moves


def findJumps(CB,player,playerTokens,opponentTokens,jumpRowInc):
    jumps=[]
    for row in VALID_RANGE:
        for col in VALID_RANGE:
            if CB[row][col] in playerTokens:
                if CB[row][col] not in [2,4]: #not a king
                    for colInc in JUMP_INCs:
                        toRow=row+jumpRowInc
                        toCol=col+colInc
                        if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY and CB[(row+toRow)//2][(col+toCol)//2] in opponentTokens:
                            jumps.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))
                else: #is a king
                    for rInc in JUMP_INCs:
                        for colInc in JUMP_INCs:
                            toRow=row+rInc
                            toCol=col+colInc
                            if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY and CB[(row+toRow)//2][(col+toCol)//2] in opponentTokens:
                                jumps.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))    
    return jumps

def expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc):
    newJumps=[]
    for oldJump in oldJumps:
        row=ord(oldJump[-2])-65
        col=int(oldJump[-1])
        newJumps.append(oldJump)
        startRow=ord(oldJump[0])-65
        startCol=int(oldJump[1])
        if CB[startRow][startCol] not in [2,4]: #not a king
            for colInc in INCs:
                jumprow=row+rowInc
                jumpcol=col+colInc
                torow=row+2*rowInc
                tocol=col+2*colInc
                if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                and CB[jumprow][jumpcol] in opponentTokens and CB[torow][tocol]==EMPTY:
                    newJumps.append(oldJump+":"+chr(torow+65)+str(tocol))
                    if oldJump in newJumps:
                        newJumps.remove(oldJump)
        else: #is a king
            for colInc in INCs:
                for newRowInc in INCs:
                    jumprow=row+newRowInc
                    jumpcol=col+colInc
                    torow=row+2*newRowInc
                    tocol=col+2*colInc
                    if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                    and CB[jumprow][jumpcol] in opponentTokens and (CB[torow][tocol]==EMPTY or oldJump[0:2]==chr(torow+65)+str(tocol)) \
                    and ((oldJump[-2:]+":"+chr(torow+65)+str(tocol)) not in oldJump) and (chr(torow+65)+str(tocol)+':'+oldJump[-2:] not in oldJump) and (chr(torow+65)+str(tocol)!=oldJump[-5:-3]):
                        newJumps.append(oldJump+":"+chr(torow+65)+str(tocol))
                        if oldJump in newJumps:
                            newJumps.remove(oldJump)
    return newJumps          

def findCrownings(CB,player,possibles):
    crownings=[]
    empties=[]
    singleCheckerPositions=[]
    if player=="gray":
        for col in range(1,8,2):
            if CB[0][col]==EMPTY:
                empties.append("A"+str(col))
        for row in range(8):
            for col in range(8):
                if CB[row][col]==3:
                    singleCheckerPositions.append(chr(row+65)+str(col))                
    else:
        for col in range(0,8,2):
            if CB[7][col]==EMPTY:
                empties.append("H"+str(col))
        for row in range(8):
            for col in range(8):
                if CB[row][col]==1:
                    singleCheckerPositions.append(chr(row+65)+str(col))
    if len(empties)!=0:
        for move in possibles["moves"]:
            if move[3:] in empties and move[0:2] in singleCheckerPositions:
                crownings.append(move)
        for jump in possibles["jumps"]:
            if jump[-2:]in empties and jump[0:2] in singleCheckerPositions:
                crownings.append(jump)
    return crownings

def findBlocks(CB,player,possibles):
    #only finds placement blocks
    if player=="gray":
        player="red"
        playerTokens=[1,2]
        opponentTokens=[3,4]
        rowInc=1
    else:
        player="gray"    
        playerTokens=[3,4]
        opponentTokens=[1,2]
        rowInc=-1
    #Find jumps for opposing player
    oldJumps=findJumps(CB,player,playerTokens,opponentTokens,rowInc)
    newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    while newJumps != oldJumps:
        oldJumps=newJumps
        newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    blocks=[]
    for move in possibles["moves"]:
        for jump in newJumps:
            for index in range(3,len(jump),3):
                if jump[index:index+2]==move[3:5]:
                    if move not in blocks:
                        blocks.append(move)
    for myJump in possibles["jumps"]:
        for myIndex in range(3,len(myJump),3):
            for jump in newJumps:
                for index in range(3,len(jump),3):
                    if jump[index:index+2]==myJump[myIndex:myIndex+2]:
                        if myJump not in blocks:
                            blocks.append(myJump)
    return blocks
        


def readCheckerFile(CB):
    fileName="gameboard.txt" #input("Enter a file name to start the game (prefix and .txt) => ")
    if fileName!="":
        inFile=open(fileName,"r")
        player=inFile.readline()
        for row in inFile:
            newRow=[]
            for item in row:
                if item !="\n":
                    newRow.append(int(item))
            CB.append(newRow)
        inFile.close()
        return player[:-1]
    else:
        newGame=[[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [3,0,3,0,3,0,3,0], [0,3,0,3,0,3,0,3], [3,0,3,0,3,0,3,0]]
        for row in newGame:
            CB.append(row)
        p=random.randint(0,1)
        if p==0:
            return "gray"
        else:
            return "red"
        
def gameIsOver(CB):
    redCount=0
    grayCount=0
    for row in CB:
        for token in row:
            if token in [1,2]:
                redCount+=1
            elif token in [3,4]:
                grayCount+=1
    if redCount==0:
        return True
    if grayCount==0:
        return True
    return False

def automatedMove(CB,player,possibles):
    #Here is where the decision-making for game play occurs
    possibles=getPossibles(CB,player,True)
    if len(possibles["jumps"])>0:
        for aMove in possibles['jumps']:
            if aMove in possibles['crownings']:
                if aMove in possibles['blocks']:
                    return aMove
                else:
                    return aMove
            elif aMove in possibles['blocks']:
                return aMove
        index=random.randint(0,len(possibles['jumps'])-1)
        return possibles['jumps'][index]
    elif len(possibles["crownings"])>0:
        for aMove in possibles['crownings']:
            if aMove in possibles['blocks']:
                return aMove
        index=random.randint(0,len(possibles['crownings'])-1)
        return possibles['crownings'][index]
    elif len(possibles["blocks"])>0:
        index=random.randint(0,len(possibles['blocks'])-1)
        return possibles['blocks'][index]
    else:        
        index=random.randint(0,len(possibles['moves'])-1)
        return possibles['moves'][index]
    
def switchPlayers(player):
    #switch players
    if player=="gray":
        player="red"
    else:
        player="gray"
    return player
   
def checkers(size):
    CB=[]
    player=readCheckerFile(CB)    
    sue=cTurtle.Turtle()
    sue.tracer(False)  
    drawCheckerBoard(sue,-4*size,4*size,size)
    labelBoard(sue,size)
    fillCheckerBoard(sue,size,CB)
    sue.tracer(True)
    possibles={}
    while not(gameIsOver(CB)):
        possibles=getPossibles(CB,player,False)
        move=automatedMove(CB,player,possibles)
        if VERBOSE:
            print("About to move "+player+" "+move)
            junk=input("Press enter to continue . . .")
        if not(validMove(CB,move,player)):
            print("Invalid Move - Game Over!")
            return
        else:
            moveChecker(sue,size,move,player,CB,possibles)
            if VERBOSE:
                showBoard(CB)
        player=switchPlayers(player)
       

checkers(60)
