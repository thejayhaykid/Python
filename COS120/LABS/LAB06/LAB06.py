#LAB06
#4.14
a=[2,8,22,6,5,8,65,8,54,84,54,65,54,654,31,465,7]
def getMin(alist):
    minSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] < minSoFar:
            minSoFar = alist[pos]

    return minSoFar
##print(getMin(a))
#4.15
def getMin2(alist):
    minSoFar=alist[0]
    for item in alist[1:]:
        if item < minSoFar:
            minSoFar = item

    return minSoFar
##print(getMin2(a))
#4.16
def getMax(alist):
    maxSoFar=alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] > maxSoFar:
            maxSoFar=alist[pos]

    return maxSoFar
def getRange(alist):
    return getMax(alist)-getMin(alist)
##print(getRange(a))
#4.17
def mean(alist):
    mean=sum(alist)/len(alist)
    return mean
##print(mean([20,32,21,26,33,22,18]))
#4.18
def mean1(alist):
    sumOfList=0
    for i in range(len(alist)):
        sumOfList=sumOfList+alist[i]
    mean=sumOfList/len(alist)
    return mean
##print(mean1([20,32,21,26,33,22,18]))
#4.20
agelist1=[18,20,21,18,19,17,20,19,18,18]
##print(mean(agelist1))
#4.21
agelist2=[18,20,21,18,19,17,20,19,18,18,39]
##print(mean(agelist2))
#4.22
def median(alist):
    copylist=alist[:]
    copylist.sort()
    if len(copylist)%2==0:
        rightmid=len(copylist)//2
        leftmid=rightmid-1
        median=(copylist[leftmid]+copylist[rightmid])/2.0
    else:
        mid=len(copylist)//2
        median=copylist[mid]
    return median
##print(median(agelist1))
#4.23
##print(median(agelist2))
#4.24
def makeDictionary(list1,list2):
    scoreDict={}
    for i in range(len(list1)):
        scoreDict[list1[i]]=list2[i]
    return scoreDict
names=["joe","tom","barb","sue","sally"]
scores=[10,23,13,18,12]
##print(makeDictionary(names,scores))
#4.25-4.30
def demoDictionaryOps(nameScoresD):
    print(nameScoresD["barb"])
    nameScoresD["john"]=19
    scoreDict= sorted(nameScoresD.items(), key=lambda x: x[1])
    print(scoreDict)
    scores=list(nameScoresD.values())
    averageScores=mean(scores)
    print(averageScores)
    nameScoresD["sally"]=13
    print(nameScoresD)
    del nameScoresD["tom"]
    print(nameScoresD)


##demoDictionaryOps(makeDictionary(names,scores))
myDictionary=makeDictionary(names,scores)
#4.31
def Alpha():
    ascending = sorted(myDictionary, key = lambda x: x[1])
    ascending.sort()
    print(ascending)
    sortedDictionary={}
    for i in range(len(ascending)):
        name=ascending[i]
        score=myDictionary.get(ascending[i])
        print(name,score)
        sortedDictionary[name]=score
    print(sortedDictionary)
##Alpha()
4.32
def getScore(name,Dictionary):
    if name not in Dictionary:
        return print("ERROR",-1)
    else:
        return Dictionary.get(name)
print(getScore("tom",makeDictionary(names,scores)))
