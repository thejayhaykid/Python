import cTurtle
from polygonPrimitives import *
center=cTurtle.Turtle()
stem=cTurtle.Turtle()
petals=cTurtle.Turtle()
#leaves=cTurtle.Turtle()

def drawStem(size):
    stem.right(90)
    stem.color("green")
    stem.pensize(size/2)
    stem.forward(250)
    stem.up()
    stem.goto(1000,1000)

def drawCenter(size):
    center.color("brown")
    center.fillcolor("brown")
    center.begin_fill()
    center.circle(size)
    center.end_fill()
    center.up()
    center.goto(1000,1000)

def drawPetals(petals1,numPetals):
    petals.up()
    petals.goto(0,(petals1+(petals1/2)))
    petals.down()
    petals.fillcolor("yellow")
    for p in range(1,numPetals):
        petals.begin_fill()
        petals.circle(petals1/2)
        petals.right(10)
        petals.forward(5)
        petals.end_fill()
    petals.up()
    petals.goto(1000,1000)
    
def drawFlower(t,numIters,size):
    drawStem(size)
    drawCenter(size)
    drawPetals(t,numIters)

drawFlower(50,50,50)
