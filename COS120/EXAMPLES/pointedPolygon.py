import cTurtle
from polygonPrimitives import *

def drawPointedPolygon(aTurtle,numOfSides,Length):
    drawPolygon(aTurtle,Length,numOfSides)
    for a in range(0,numOfSides):
        aTurtle.left(60)
        aTurtle.forward(Length)
        aTurtle.right(120)
        aTurtle.forward(Length)
        aTurtle.left(60)
        aTurtle.right(360/numOfSides)

sue=cTurtle.Turtle()
drawPointedPolygon(sue,12,100)
