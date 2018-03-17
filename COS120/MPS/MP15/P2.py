EMPTY=0
INCs=[-1,1]
VALID_RANGE=range(8)
DEBUG=False
VISIBLE=True
from copy import *
from math import *
import random

def getPossibles(CB,player):
    possibles={}
    if player=="black":
        playerTokens=[3,4]
        opponentTokens=[1,2]
        rowInc=-1
    else:
        playerTokens=[1,2]
        opponentTokens=[3,4]
        rowInc=1
    possibles["moves"]=findMoves(CB,player,playerTokens,opponentTokens,rowInc)  #puts moves right into possibles D      
    oldJumps=findJumps(CB,player,playerTokens,opponentTokens,rowInc)
    newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    while newJumps != oldJumps:
        oldJumps=newJumps
        newJumps=expandJumps(CB,player,oldJumps,playerTokens,opponentTokens,rowInc)
    possibles["jumps"]=newJumps
    possibles["crownings"]=findCrownings(CB,player,possibles)
    possibles["blocks"]=findBlocks(CB,player,possibles)
    return possibles

def findBlocks(CB,player,possible):
    #only finds placement blocks
    if player=="black":
        player="red"
        playerTokens=[1,2]
        opponentTokens=[3,4]
        rowInc=1
    else:
        player="black"    
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
    for move in possible["moves"]:
        for jump in newJumps:
            for index in range(3,len(jump),3):
                if jump[index:index+2]==move[3:5]:
                    if move not in blocks:
                        blocks.append(move)
    for myJump in possible["jumps"]:
        for myIndex in range(3,len(myJump),3):
            for jump in newJumps:
                for index in range(3,len(jump),3):
                    if jump[index:index+2]==myJump[myIndex:myIndex+2]:
                        if myJump not in blocks:
                            blocks.append(myJump)
    return blocks
        
def findCrownings(CB,player,possibles):
    crownings=[]
    empties=[]
    singleCheckerPositions=[]
    if player=="black":
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

def findMoves(CB,player,playerTokens,opponentTokens,rowInc):
    moves=[]
    #process all board positions    
    for row in range(8):
        for col in range(8):
            if CB[row][col] in playerTokens:
                if CB[row][col] not in [2,4]: #not a king
                    for colInc in INCs:
                        toRow=row+rowInc
                        toCol=col+colInc
                        if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY:
                                moves.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))
                else: #a king
                    for rInc in INCs:
                        for colInc in INCs:
                            toRow=row+rInc
                            toCol=col+colInc
                            if toRow in VALID_RANGE and toCol in VALID_RANGE and CB[toRow][toCol]==EMPTY:
                                    moves.append(chr(row+65)+str(col)+":"+chr(toRow+65)+str(toCol))
                       
    return moves

def findJumps(CB,player,playerTokens,opponentTokens,rowInc):
    jumps=[]
    for row in range(8):
        for col in range(8):
            if CB[row][col] in playerTokens: #if this is a player piece
                if CB[row][col] not in [2,4]: #not a king
                    for colInc in INCs: #-1 and 1
                        jump=chr(row+65)+str(col)+":"
                        jumprow=row+rowInc
                        jumpcol=col+colInc
                        torow=row+2*rowInc
                        tocol=col+2*colInc
                        if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                        and CB[jumprow][jumpcol] in opponentTokens and CB[torow][tocol]==EMPTY:
                            jumps.append(jump+chr(torow+65)+str(tocol))
                else: #is a king
                    for colInc in INCs: #-1 and 1
                        for newRowInc in INCs:
                            jump=chr(row+65)+str(col)+":"
                            jumprow=row+newRowInc
                            jumpcol=col+colInc
                            torow=row+2*newRowInc
                            tocol=col+2*colInc
                            if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                            and CB[jumprow][jumpcol] in opponentTokens and CB[torow][tocol]==EMPTY:
                                jumps.append(jump+chr(torow+65)+str(tocol))
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
                    and ((oldJump[-2:]+":"+chr(torow+65)+str(tocol)) not in oldJump) and ((chr(torow+65)+str(tocol)+':'+oldJump[-2:] not in oldJump)) and (chr(torow+65)+str(tocol)!=oldJump[-5:-3]):
                        newJumps.append(oldJump+":"+chr(torow+65)+str(tocol))
                        if oldJump in newJumps:
                            newJumps.remove(oldJump)
    return newJumps          

#Not very intelligent player
def automatedMove(CB,player):
    possibles=getPossibles(CB,player)
    if len(possibles["jumps"])>0:
        index=random.randint(0,len(possibles["jumps"])-1)
        if DEBUG:
##            print("About to jump ",possibles["jumps"][index])
            junk=input()
        return possibles["jumps"][index]
    index=random.randint(0,len(possibles["moves"])-1)
    return possibles["moves"][index]
