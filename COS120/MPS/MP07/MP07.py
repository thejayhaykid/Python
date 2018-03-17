##I start by drawing the board. I then place all of the checkers.
##I then move the top left black checker up and right 1, I then move the middle right black up 2 left 2
##I then move the bottom left red down 2 right 2 and remove the second black
from turtle import *
side = 75
COUNT = 8
column=[-300,-225,-150,-75,0,75,150,225,300]
row=[300,225,150,75,0,-75,-150,-225,-300]
def DrawBox(count,colorcount,side):
    # determine color
    if colorcount%2==0:
        if count % 2 == 1:
            fillcolor('#000000')
        else:
            fillcolor('#990000')
    else:
        if count % 2 == 1:
            fillcolor('#990000')
        else:
            fillcolor('#000000')
    
    # draw box
    begin_fill()
    for i in range(4):
        forward(side)
        left(90)
    end_fill()



def board(sidelen):
    p=2
    up()
    goto(sidelen*-4,sidelen*-4)
    down()
    for l in range(COUNT):
        tracer(False)
        for i in range(COUNT):
            DrawBox(i,p,sidelen)
            forward(sidelen)
        p+=1
        up()
        goto(sidelen*-4,(((l+1)*sidelen)+(sidelen*-4)))
        down()
        tracer(True)
        
def drawPolygon(sideLength,numSides,color):
    turnAngle=360/numSides
    fillcolor(color)
    pencolor("#777777")
    begin_fill()
    for i in range(numSides):
        forward(sideLength)
        right(turnAngle)
    end_fill()
    pencolor("#000000")

        
        
def drawCircle(radius,Color):
    tracer(False)
    circumference=2*3.1415*radius
    sideLength=circumference/360
    fillcolor(Color)
    drawPolygon(sideLength,360,Color)
    tracer(True)
    
    
def drawChecker(locx,locy,color):
    up()
    goto(locx,locy)
    down()
    drawCircle(37,color)
    up()
    goto(locx,locy-10)
    down()
    drawCircle(27,color)


    
def moveChecker(fromRow,fromCol,toRow,toCol,color):
    speed(1000)
    up()
    goto(row[fromRow],column[fromCol])
    down()
    DrawBox(0,2,75)
    up()
    goto(column[toCol],row[toRow])
    down()
    drawChecker(row[toRow]+(side/2),column[toCol],color)
    

    
def startingPositionsBlack(x,sideLength,posneg,color,counter):
    tracer(False)
    counter2=1
    y=(sideLength*posneg*4)+75
    for j in range(3):
        for i in range(4):
            drawChecker(x,y,color)
            x=x+150
        if counter%2==1:
            x=sideLength*(posneg)*4+37.5
        else:
            x=sideLength*-3+37.5
        y=(sideLength*posneg*(4-counter2))+75
        counter+=1
        counter2+=1
    tracer(True)

def startingPositionsRed(x,sideLength,posneg,color,counter):
    tracer(False)
    counter2=1
    y=(sideLength*4)
    for j in range(3):
        for i in range(4):
            drawChecker(x,y,color)
            x=x+150
        if counter%2==1:
            x=sideLength*-3+37.5
        else:
            x=sideLength*-4+37.5
        y=(sideLength*(4-counter2))
        counter+=1
        counter2+=1
    tracer(True)
    
def main():
    tracer(False)
    board(75)
    x=side*-4+(side/2)
    startingPositionsBlack(x,75,-1,"#000000",2)
    x=side*-3+(side/2)
    startingPositionsRed(x,75,-1,"#990000",2)
    moveChecker(8,2,7,4,"#000000")
    moveChecker(4,2,6,5,"#000000")
    moveChecker(7,5,5,4,"#990000")
    moveChecker(6,4,5,4,"#990000")
    tracer(True)

main()
