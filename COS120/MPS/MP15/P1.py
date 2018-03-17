import cTurtle
import math
import random

EMPTY=0
INCs=[-1,1]
JUMP_INCs=[-2,2]
VALID_RANGE=range(8)
VERBOSE=False
VISIBLE=True

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
            if player=="gray" or player=='black':
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

def getPossibles(CB,player,VERBOSE):
    possibles={}
    if player=="gray" or player=='black':
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
    if VERBOSE == True:
        print("Moves for "+player+" = ",possibles["moves"])
        print("Jumps for "+player+" = ",possibles["jumps"])
        print("Crownings for "+player+" = ",possibles["crownings"])
        print("Blocks for "+player+" = ",possibles["blocks"])
    return possibles

def validMove(CB,move,player):
    possibles=getPossibles(CB,player,VERBOSE)
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
    VALID_RANGE=range(8)
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
    if player=="gray" or player=='black':
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
    if player=="gray" or player=='black':
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

def automatedMove(CB,player):
    if player=='black':
        player=='gray'
    #Here is where the decision-making for game play occurs
    possibles=getPossibles(CB,player,VERBOSE)
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
