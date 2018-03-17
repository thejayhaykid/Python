import cTurtle
from polygonPrimitives import *

def drawPointedPolygon(aTurtle,LengthOfSide,numOfSides):
    drawPolygon(aTurtle,LengthOfSide,numOfSides)
    for i in range(numOfSides):
        aTurtle.left(60)
        aTurtle.fd(LengthOfSide)
        aTurtle.right(120)
        aTurtle.fd(LengthOfSide)
        aTurtle.left(60)
        aTurtle.right(360/numOfSides)



sue=cTurtle.Turtle()
drawPointedPolygon(sue,100,9)
