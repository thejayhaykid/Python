import cTurtle
bob=cTurtle.Turtle()

def oneThirdPoint(p1,p2):
    return ((p1[0]-p2[0])/3.0,(p1[1]-p2[1])/3.0)

def drawSquare(t,p1,p2,p3,p4,color):
    t.color(color,color)
    t.up()
    t.goto(p1)
    t.down()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)
    t.goto(p1)
    t.end_fill()


def recSquare(myTurtle,p1,p2,p3,p4,depth):
    colorlist = ['red','green','black','blue','#880088']
    drawSquare(myTurtle,p1,p2,p3,p4,colorlist[depth])
    if depth > 0 :
            x3 = oneThirdPoint(p3,p2)[0]
            y3 = oneThirdPoint(p2,p1)[1]
            print("1",depth)
            recSquare(myTurtle,p1,(p1[0],p1[1]+y3),(p1[0]+x3,p1[1]+y3),(p1[0]+x3,p1[1]),depth-1)
            print("2",depth)
            recSquare(myTurtle,(p2[0],p2[1]-y3),p2,(p2[0]+x3,p2[1]),(p2[0]+x3,p2[1]-y3),depth-1)
            print("3",depth)
            recSquare(myTurtle,(p3[0]-x3,p3[1]-y3),(p3[0]-x3,p3[1]),p3,(p3[0],p3[1]-y3 ),depth-1)
            print("4",depth)
            recSquare(myTurtle,(p4[0]-x3,p4[1]),(p4[0]-x3,p4[1]+y3),(p4[0],p4[1]+y3),p4,depth-1)
            print("5",depth)



def Zooper(n):
    if(n>3):
        print(" N=",n," ",end="")
        print("0",end="")
        Zooper(n-1)
        print(" n=",n," ",end="")
        print("1",end="")
        Zooper(n-1)
        

recSquare(bob,(100,100),(100,-100),(-100,-100),(-100,100),2)
Zooper(6)
