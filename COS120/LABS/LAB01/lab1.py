#L01-1
a=1
for a in range(1,11):
    print(a)
print("-----------------")
#L01-2
for b in range(10,0,-1):
    print(b)
print("-----------------")
#L01-3
for c in range(3,34,3):
    print(c)
print("-----------------")
#L01-4
for d in range(33,2,-3):
    print(d)
print("-----------------")
#L01-5
startNum=d
stepNum=b
stopNum=a
for e in range(startNum,stopNum,stepNum):
    print(e)
print("-----------------")
#L01-6
startNum=d
stepNum=b
stopNum=a
e3=0
for e2 in range(startNum,stopNum,stepNum):
    e3=e3+e2
print(e3)
print("-----------------")
#L01-7
def printSeries(startNum,stopNum,stepNum):
    for f in range(startNum,stopNum,stepNum):
        print(f)
print(printSeries(1,14,2))
print("-----------------")
#L01-8
def sumIntsToN(N):
    g1=0
    g2=1
    for g in range(1,N+1):
        g1=g1+g2
        g2=g2+1
    print(g1)
    return(g1)
sumIntsToN(5)
print("-----------------")
#L01-9
4*sumIntsToN(5)
#this only works in the shell as it will on print g1 just from running the program.
print("-----------------")
#L01-10
def sumOddIntsToN(M):
    h1=0
    h2=1
    for h in range(1,M+1,2):
        h1=h1+h2
        h2=h2+2
    print(h1)
    return(h1)
sumOddIntsToN(5)
print("-----------------")
#L01-11
def sumEvenIntsToN(O):
    i1=0
    i2=2
    for i in range(2,O+1,2):
        i1=i1+i2
        i2=i2+2
    print(i1)
    return(i1)
sumOddIntsToN(5)
print("-----------------")
#L01-12
def displayIntSumsToN(Q):
    print("The sum of the integers from 1 to",Q,"is",sumIntsToN(Q))
    print("The sum of the odd integers from 1 to",Q,"is",sumOddIntsToN(Q))
    print("The sum of the even integers from 1 to",Q,"is",sumEvenIntsToN(Q))
displayIntSumsToN(8)
print("-----------------")
#L01-13
import cTurtle
crush=cTurtle.Turtle()
crush.up()
for x in range(-25,25,1):
    y=x**2
    crush.goto(x,y)
    crush.dot()
print("-----------------")
#L01-14
crush1=cTurtle.Turtle()
crush1.up()
for x1 in range(-250,250,5):
    y1=(x1/2)+3
    crush1.goto(x1,y1)
    crush1.dot()
print("-----------------")
print("END")
