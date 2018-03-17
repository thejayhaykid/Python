#Machine Problem 5 for Jake Hayes
def listMatchCount(a,b):
    count=0
    newList=[]
    for item in a+b:
        if item in b and item in a and item not in newList:
            count+=1
            newList.append(item)
    print(newList)
    return count
def listMatchCountTest():
    a=[3,1,3,2]
    b=[5,1,5,6,3]
    c=[1,2,3,4,5,6]
    d=["a","b","c","d"]
    e=[3,3,3,3,3,3]
    print(listMatchCount(a,b))
    print(listMatchCount(d,b))
    print(listMatchCount(a,c))
    print(listMatchCount(a,e))
    print(listMatchCount(c,e))
listMatchCountTest()
