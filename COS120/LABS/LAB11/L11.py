#Lab 11 for Jake Hayes
#L11-1 -- 9.1
import cTurtle
bob=cTurtle.Turtle()
def drawSquare(aTurtle,side):
    aTurtle.setheading(0)
    for i in range(4):
        aTurtle.forward(side)
        aTurtle.right(90)

def nestedBox(aTurtle,side):
    if side >= 1:
        nestedBox(aTurtle,side-5)
        drawSquare(aTurtle,side)


#L11-2
def drawCenteredSquare(aTurtle,centerX,centerY,side):
    if side >=1:
        half=side/2
        aTurtle.up()
        aTurtle.goto(centerX-half,centerY+half)
        aTurtle.down()
        drawSquare(aTurtle,side)
        drawCenteredSquare(aTurtle,centerX,centerY,side-7)



#L11-3
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
##print(fact(7))

#L11-4
def sumOfList(aList):
    sum = 0
    for element in aList:
        if type(element) == type([]):
            sum = sum + sumOfList(element)
        else:
            sum = sum + element
    return sum
myList=[8,4,8,9,6,5,2,3]

#L11-5
def recursiveMin(aList):
    smallest = aList[0]
    while type(smallest) == type([]):
        smallest = smallest[0]

    for element in aList:
        if type(element) == type([]):
            min_of_elem = recursiveMin(element)
            if smallest > min_of_elem:
                smallest = min_of_elem
        else:                           
            if smallest > element:
                smallest = element

    return smallest

##nestedBox(bob,200)
##drawCenteredSquare(bob,0,0,200)
##print(sumOfList(myList))
##print(recursiveMin(myList))


bob.up()
bob.goto(0,-30)
bob.setheading(90)
bob.backward(100)
bob.down()


#L11-6
def tree(trunkLength,t):
    if trunkLength >= 5:
        t.forward(trunkLength)
        t.right(30)
        tree(trunkLength-10,t)
        t.left(60)
        tree(trunkLength-10,t)
        t.right(30)
        t.backward(trunkLength)
    else:
        return
        

#L11-7
def tree2(trunkLength,t):
    if trunkLength >= 5:
        t.forward(trunkLength)
        t.left(30)
        tree(trunkLength-10,t)
        t.right(60)
        tree(trunkLength-10,t)
        t.left(30)
        t.backward(trunkLength)
    else:
        return


from random import *

#L11-8
def tree3(trunkLength,t):
    turn1 = randrange(15,45)
    turn2 = randrange(15,45)
    if trunkLength >= 5:
        t.forward(trunkLength)
        t.right(turn1)
        tree(trunkLength-10,t)
        t.left(turn2)
        tree(trunkLength-10,t)
        t.right(turn1)
        t.backward(trunkLength)
    else:
        return


#L11-9
def tree4(trunkLength,t):
    turn1 = randrange(15,45)
    turn2 = randrange(15,45)
    shrinkRate = randrange(5,25)
    if trunkLength >= 5:
        t.forward(trunkLength)
        t.right(turn1)
        tree(trunkLength-shrinkRate,t)
        t.left(turn2)
        tree(trunkLength-shrinkRate,t)
        t.right(turn1)
        t.backward(trunkLength)
    else:
        return

##tree(50,bob)
##tree2(50,bob)
##tree3(50,bob)
##tree4(50,bob)
