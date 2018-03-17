#H2 for Jake Hayes
import cTurtle
import polygonPrimitives
import math
###1.22
##sven=cTurtle.Turtle()
##sven.forward(10)
###sven's position is (10,0)
###1.23
##ole=cTurtle.Turtle()
##ole.right(45)
##ole.forward(50)
###1.24
##zach=cTurtle.Turtle()
##zach.right(50)
##zach.forward(75)
##zach.right(130)
##zach.forward(75)
##zach.right(50)
##zach.forward(75)
##zach.right(130)
##zach.forward(75)
###1.25
##t=cTurtle.Turtle()
##Len=50
##turnAngle=360/4
##for i in range(2):
##    t.forward(Len)
##    t.right(turnAngle)
##    t.forward(Len*2)
##    t.right(turnAngle)
###1.26
##r=cTurtle.Turtle()
##def drawRectangle(r,length,width):
##    turnAngle=360/4
##    for i in range(2):
##        r.forward(length)
##        r.right(turnAngle)
##        r.forward(width)
##        r.right(turnAngle)
##    
##drawRectangle(r,25,50)
###1.28
##l=cTurtle.Turtle()
##drawRectangle(l,50,300)
###1.30
##for q in range(5,51,5):
##    print(q)
###1.31
##for john in range(-10,11):
##    print(john)
###1.32
##for m in range(10,-11,-1):
##    print(m)
#1.33
p=cTurtle.Turtle()
p.tracer(False)
for j in range(250,0,-1):
    p.right(135)
    p.forward(j)
p.tracer(True)
###1.34
##o=cTurtle.Turtle()
##for s in range(150,0,-1):
##    o.right(45)
##    o.forward(s)
###1.35
##u=cTurtle.Turtle()
##for a in range(150,0,-1):
##    u.right(a)
##    u.forward(100)
###1.36
##o1=cTurtle.Turtle()
##o2=cTurtle.Turtle()
##for s1 in range(150,0,-1):
##    o1.right(90)
##    o1.forward(s1)
##    o2.left(90)
##    o2.forward(s1)
###1.37
##def drawTriangle(angle,side1,side2):
##    side3=math.sqrt(side1**2+side2**2)
##    tri=cTurtle.Turtle()
##    tri.forward(side1)
##    tri.right(angle)
##    tri.forward(side2)
##    if side1==side2:
##        angle2=(180-angle)/2
##    tri.right(90+angle2)
##    tri.forward(side3)
##
##drawTriangle(90,100,100)
###1.38
##ss1=cTurtle.Turtle()
##def seriesSquare():
##    for ss in range(100,-1,-5):
##        polygonPrimitives.drawSquare(ss1,ss)
##seriesSquare()
###1.39
##dd1=cTurtle.Turtle()
##def seriesSquare2():
##    x1=0
##    y1=0
##    for dd in range(100,-1,-5):
##        polygonPrimitives.drawSquare(dd1,dd)
##        dd1.up()
##        dd1.goto(x1,y1)
##        dd1.down()
##        x1=x1+3
##        y1=y1-3
##seriesSquare2()
