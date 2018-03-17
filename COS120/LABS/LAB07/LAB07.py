w=[83,99,2,3,1,7,54,1]
x=[23,12,67,5,4,11,2,84,12,16]
y={"staplers":2,"pencils":45,"erasers":12,"paper clips":200, "pens":84,"markers":12}
z={23012:2,77321:5,32332:234,77656:16,21321:802,99876:3}

#L07-01
def printOutList(l1):
    print("L07-01:")
    print(l1)
##printOutList(w)
#L07-02
def printOutDict(D):
    print("L07-02:")
    print(D)
##printOutDict(y)
#L07-03
def printByKey(D):
    print("L07-03:")
    sorted_list = [x for x in D.items()]
    sorted_list.sort(key=lambda x: x[0])
    print(sorted_list)
##printByKey(y)
#L07-04
def printByValue(D):
    print("L07-04:")
    sorted_list = [x for x in D.items()]
    sorted_list.sort(key=lambda x: x[1])
    print(sorted_list)
##printByValue(y)
#L07-05
def addToList(aList):
    print("L07-05:")
    x=input("Enter a value:")
    aList.append(int(x))
    return aList
##print(addToList(x))
#L07-06
def addToDict(D):
    print("L07-06:")
    key1=input("Enter a key:")
    value1=input("Enter a value:")
    D[key1]=value1
    return(D)
##print(addToDict(y))
#L07-07
def checkValue(D):
    print("L07-07:")
    checkKey=input("Enter a key:")
    if checkKey in D:
        return D[checkKey]
    else:
        return("NOT IN DICTIONARY")
##print(checkValue(y))
#L07-08
def checkForValue(D):
    print("L07-08:")
    checker=input("Enter a value:")
    intChecker=int(checker)
    for i in D:
        if intChecker==D[i]:
            return True
    return False
##print(checkForValue(y))
#L07-09
l = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2']
def sortList(l):
    print("L07-09:")
    numbersPerLetter = 2
    lsorted = []
    for i in range(len(l) // numbersPerLetter):
       lsorted.extend([l[x+i] for x in range(0, len(l), len(l) // numbersPerLetter)])
    print(lsorted)
##sortList(l)
#L07-10
list1=[1,2,3,4,5,6,7,8,9]
list2=[10,11,12,13,14,15,16,17,18,19]
def combineLists(l1,l2):
    print("L07-10:")
    combinedList=[]
    for i in l1:
        combinedList.append(i)
    for j in l2:
        combinedList.append(j)
    return combinedList
##print(combineLists(list1,list2))
#L07-11
def combineLists2(l1,l2):
    print("L07-11:")
    combinedList=[]
    for i in l1:
        combinedList.append(i)
    for j in l2:
        combinedList.append(j)
    combinedList.sort()
    return combinedList
##print(combineLists2(w,x))

#L07-12
from cTurtle import *
import cTurtle
listPoints=[[39,2],[16,5],[14, 99],[2,1],[28,12],[12,28],[20,50],[38,77]]
def drawAxis(minx,maxx,miny,maxy):
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
##    print(minx,maxx,miny,maxy)
    
def turtleWorld(minx,maxx,miny,maxy,pointList):
    print("L07-12:")
    xmax=0
    xmin=0
    ymax=0
    ymin=0
    for i in pointList:
        if i[0]>xmax:
            xmax=i[0]
        elif i[0]<xmin:
            xmin=i[0]
        if i[1]>ymax:
            ymax=i[1]
        elif i[1]<ymin:
            ymin=i[1]
    xmax=xmax+10
    xmin=xmin-10
    ymax=ymax+10
    ymin=ymin-10
##    print(xmax,xmin,ymax,ymin)
    setWorldCoordinates(xmin,ymin,xmax,ymax)
    drawAxis(xmin+10,xmax-10,ymin+10,ymax-10)
    up()
    for j in pointList:
        goto(j[0],j[1])
        dot()

##turtleWorld(-150,-150,150,150,listPoints)

#L07-13
homonyms=[["pie","pi"],["c","see","sea","si"]]
def homonym(aList):
    print("L07-13:")
    D={}
    for j in aList:
##        print(j)
        for i in range(len(j)):
            for k in range(len(j)):
                D.setdefault(j[i],[]).append(j[k])
##            print(i)
##            print(j[i])

    return D
print(homonym(homonyms))
