#LAB05 by Jake Hayes
#1
def showListFunctions(myClasses):
    print(myClasses[1:3])
    if "COS 120" in myClasses:
        print("IT'S IN THERE!")
    myClasses2=myClasses+myClasses[1:3]
    print(myClasses2)
    print(myClasses2[6])
    print(len(myClasses))
    print(myClasses*3)
    occ=myClasses.index("BIB 110")
    print("BIB 110 found at index",occ)

classList=["COS 120","MAT 151","BIB 110","PHP 200z","IAS 110"]
classTime=["100","1200","1100","330","1000"]
##showListFunctions(classList)
#2
def showTimeForClass(classes,times):
    i=input("Enter a course designation =>")
    j=classes.index(i)
    return times[j]

##print(showTimeForClass(classList,classTime))
#3
combined=classList+classTime
def showTimeForClass2(combined):
    i=input("Enter a course designation =>")
    j=combined.index(i)
    j+=5
    return combined[j]
##print(showTimeForClass2(combined))
#4
def demoListMethods(aList):
    aList.append("IAS 170")
    print(aList)
    aList.insert(1,"ENG 110")
    print(aList)
    print(aList.pop())
    print(aList.pop(3))
    aList.sort()
    print(aList)
    aList.reverse()
    print(aList)
    print(aList.index("MAT 151"))
    print(aList.count("MAT 151"))
    aList.remove("MAT 151")
    print(aList)
##demoListMethods(classList)
#5
def reverseList(aList):
    a=len(aList)
    bList=[]
    for i in range(len(aList)):
        bList.append(aList[a-1])
        a=a-1
    return bList
numList=[1,2,3,4,5,6,7,8,9]
print(reverseList(numList))
def reverseList2(aList):
    bList=[]
    for i in reversed(aList):
        j=i-1
        bList.append(aList[j])
    return bList
print(reverseList2(numList))
def reverseList3(aList):
    bList=[]
    for i in reversed(aList):
        j=i-1
        b=aList.pop(j)
        bList.append(b)
    return bList
print(reverseList3(numList))
#6
listA=[1200,1300,1200,1200,1500,1500,1200]
def count(aList,itemToCount):
    counter=0
    for i in range(len(aList)):
        if aList[i]==itemToCount:
            counter+=1
    return counter
##print(count(listA,1200))
def inList(aList,itemToFind):
    for i in range(len(aList)):
        if aList[i]==itemToFind:
            return True
    return False
##print(inList(listA,1500))
def find(aList,itemToFind):
    for i in range(len(aList)):
        if aList[i]==itemToFind:
            return i
    return
##print(find(listA,1500))
def insert(aList,loc,anItem):
    for i in range(len(aList)):
        if i==loc:
            cList=[anItem]
            bList=aList[:i]
            dList=aList[i:]
            eList=bList+cList+dList
    return eList
##print(insert(listA,3,"HELLO"))
def popatIndex(aList,index):
    for i in range(len(aList)):
        if i==index:
            b=aList[index]
            aList=aList[:i-1]+aList[i+1:]
            return b
##print(popatIndex(listA,4))
#7
from random import *
def shuffle(aList):
    bList=[]
    for i in range(len(aList)):
##        print(i)
        j=randint(0,len(aList)-1)
        if aList[j] not in bList:
            bList.append(aList[j])
        else:
            if j==len(aList):
                bList.append(aList[j-1])
            else:
                bList.append(aList[j+1])
    return bList
listB=[1,2,3,4,5,6,7,8,9]
##print(shuffle(listB))
#8
def shuffle2(aList):
    bList=[]
    for i in range(len(aList)):
##        print(i)
        x=len(aList)-1
        c=randint(0,x)
##        print(c)
        b=aList.pop(c)
##        print(b)
        bList.append(b)
    return bList
##print(shuffle2(listB))
