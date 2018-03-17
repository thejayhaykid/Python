#MP09 for Jake Hayes
from math import *
from cTurtle import *

a=[1,3,7,7,1,1,3,7,7]
b=["a","b","a","d","c","d"]
def calculateFD(aList):
    aList.sort()
    variableprevious=aList[0]
##    print(aList)
##    print("ITEM","FREQUENCY")
    groupcount=0
    D={}
    for i in aList:
        if i==variableprevious:
            groupcount=groupcount+1
        else:
            D[variableprevious]=groupcount
            variableprevious=i
            groupcount=1
    D[variableprevious]=groupcount
##    print(D)
    return D

def drawAxis(minx,maxx,miny,maxy):
    tracer(False)
    minx=minx*-1
    miny=miny*-1
    forward(maxx)
    right(180)
    forward(minx+maxx)
    right(180)
    forward(minx)
    right(90)
    forward(miny)
    right(180)
    forward(miny+maxy)
    right(90)
    goto(0,0)
    setheading(0)
    tracer(True)

def remove_duplicates(l):
    return list(set(l))

def labelGraph(Y,YValues,XValues,B):
    tracer(False)
    AxisLabelLength=100/Y
    YValues.sort()
    XValues.sort()
    YValues.reverse()
    XValues.reverse()
    up()
    goto(-5,95)
    y=95-AxisLabelLength
    x=95-AxisLabelLength
    remove_duplicates(YValues)
    remove_duplicates(XValues)
    print(YValues,"= YValues")
    print(XValues,"= XValues")
    D={}
    for i in YValues:
        write(i,True)
        goto(-5,y)
        B[i]=ycor()
        y=y-AxisLabelLength
    goto(95,-5)
    for j in XValues:
        write(j,True)
        goto(x,-5)
        goto(x,0)
        D[j]=pos()
        goto(x,-5)
        x=x-AxisLabelLength
    tracer(True)
    return D

def graph(C,D):
    DKeys=list(D.keys())
    DValues=list(D.values())
    PosValues=list(C.values())
    Diviser=100/len(DValues)
    print(PosValues[1][0])
    print(DKeys)
    for i in DKeys:
        print(i)
        print(C[i])
        setheading(90)
        goto(C[i][0]+Diviser,C[i][1])
        down()
        forward(50)
        up()
    

def printFrequencyDistributionD(D):
    DKeys=list(D.keys())
    DValues=list(D.values())
    DMax=max(DValues)
    DMin=min(DValues)
##    print(DKeys,DValues,DMax,DMin)
    setWorldCoordinates(-10,-10,110,110)
    drawAxis(0,100,0,100)
    B={}
    C=labelGraph(len(DValues),DValues,DKeys,B)
    print(C)
    print(B)
##    print(C[7][0])
    graph(C,D)
    
    
    

D1=calculateFD(a)
D2=calculateFD(b)
##printFrequencyDistributionD(D1)
printFrequencyDistributionD(D2)
