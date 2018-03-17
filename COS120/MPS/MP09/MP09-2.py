from cTurtle import *

def calculateFD(alist):
    countdict={}

    for item in alist:
        if item in countdict:
            countdict[item]=countdict[item]+1
        else:
            countdict[item]=1
    return countdict

def printFrequencyDistribution(countdict):
    itemlist=list(countdict.keys())
    minitem=0
    maxitem=len(itemlist)-1

    countlist=countdict.values()
    maxcount=max(countlist)

    chartT=Turtle()
    chartT.setWorldCoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem,0)
    chartT.up()

    chartT.goto(-1,0)
    chartT.write("0",font=("Arial",16,"bold"))
    chartT.goto(-1,maxcount)
    chartT.write(str(maxcount),font=("Arial",16,"bold"))

    for index in range(len(itemlist)):
        chartT.goto(index,-1)
        chartT.write(str(itemlist[index]),font=("Arial",16,"bold"))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()
    chartT.exitOnClick()

list1=[1,2,5,5,4,2,1,5,3,5,9,7,5]
list2=['a','d','e','d','c','b','g','e','g','s','a','e','a']
list3=[25,27,89,63,5,14,58,78]
D=calculateFD(list1)
printFrequencyDistribution(D)
printFrequencyDistribution(calculateFD(list2))
printFrequencyDistribution(calculateFD(list3))
