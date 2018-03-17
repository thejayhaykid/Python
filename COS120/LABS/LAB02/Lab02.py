###Lab 2 for Jake Hayes
from math import *
import cTurtle
###2.1
#####help('cTurtle')
#####2.2
#####if the quote marks are not included, cTurtle needs to be already imported for it to work.
#####help(cTurtle)
#####2.3
####import cTurtle
####help(cTurtle)
#####2.4
####import math
####help(math.sin)
#####2.5
##import random
###help(random)
##def randomSequencer(N):
##    x=random.randint(1,100)
##    for y in range(1,N+1):
##        l=random.randint(1,100)
##        print(l)
##randomSequencer(2)
#####2.6
##def archimedes(numsides):
##    innerangleB=360/numsides
##    halfangleA=innerangleB/2
##    onehalfsideS=sin(radians(halfangleA))
##    sideS=onehalfsideS*2
##    polygonCircumference=numsides*sideS
##    pi=polygonCircumference/2
##    return pi
##print(archimedes(1000000000))
##print(pi)
##print("Archimedes function ran 1000000000 times and they are equal.")
###2.7
##import math
##def archimedesRadius(numsides,radius):
##    innerangleB=360/numsides
##    halfangleA=innerangleB/2
##    onehalfsideS=math.sin(math.radians(halfangleA))
##    sideS=onehalfsideS*2
##    polygonCircumference=numsides*sideS
##    pi1=polygonCircumference/(2*radius)
##    return pi1
##print(archimedesRadius(1000000000,5))
###2.8
##def sumOfEvens():
##    total=0
##    for n in range(0,101,2):
##        total=total+n
##    return total
##print(sumOfEvens())
#####2.9
##def sumOfOdds():
##    total1=0
##    for n in range(1,51,2):
##        total1=total1+n
##    return total1
##print(sumOfOdds())
#####2.10
##def averageOfOdd():
##    average=0
##    total2=0
##    for n in range(1,201,2):
##        total2=total2+n
##    average=total2/100
##    return average
##print(averageOfOdd())
###2.11
##def averageOfN(N):
##    average=0
##    total2=0
##    for n in range(1,N+1,1):
##        total2=total2+n
##    average=total2/N
##    return average
##print(averageOfN(100))
###2.12
##def factorial(N):
##    product=1
##    for i in range(1,N+1):
##        product=product*i
##    return product
##print(factorial(5))
#2.13
def fibo():
    x1=0
    x2=0
    check=0
    total=1
    newList=[]
    for i in range(1,10):
        if check==0:
            x1=total
            check=check+1
            newList.append(x1)
        else:
            x2=total
            check=check-1
            newList.append(x2)
        total=x1+x2
    print(newList)
    return total
print(fibo())
#2.14
def fibo1(N):
    x1=0
    x2=0
    check=0
    total=1
    for i in range(1,N):
        if check==0:
            x1=total
            check=check+1
        else:
            x2=total
            check=check-1
        total=x1+x2
    return total
print(fibo1(14))
###2.15
##def leibniz(terms):
##    acc=0
##    num=4
##    den=1
##    for aterm in range(terms):
##        nextterm=num/den*(-1)**aterm
##        acc=acc+nextterm
##        den=den+2
##    return (acc)
##print(leibniz(10000))
##print(leibniz(100000))
###2.16
##def leibniz1(terms):
##    acc=0
##    num=4
##    den=1
##    for aterm in range(terms):
##        nextterm=num/den*(-1)**aterm
##        acc=acc+nextterm
##        den=den+2
##    return (acc)
##print(leibniz1(10000))
##def archimedes1(numsides):
##    innerangleB=360/numsides
##    halfangleA=innerangleB/2
##    onehalfsideS=sin(radians(halfangleA))
##    sideS=onehalfsideS*2
##    polygonCircumference=numsides*sideS
##    pi=polygonCircumference/2
##    return pi
##print(archimedes1(10000))
##print(pi)
###2.17
##def leibniz2(terms):
##    acc=0
##    num=4
##    den=1
##    for aterm in range(terms):
##        nextterm=num/den*(-1)**aterm
##        acc=acc+nextterm
##        den=den+2
##        if den>0:
##            den=den*1
##        else:
##            den=den*-1
##    return (acc)
##print(leibniz2(10000))
###2.18
##def star(t,n,l):
##    for i in range(n):
##        t.left(60)
##        t.fd(l)
##        t.right(120)
##        t.fd(l)
##        t.left(60)
##        t.right(360/n)
##t=cTurtle.Turtle()
##star(t,3,50)
##star(t,4,50)
##star(t,5,50)
##star(t,6,50)
##star(t,7,50)
##star(t,8,50)
##star(t,9,50)
###2.19
##def sky(numStars):
##    p=cTurtle.Turtle()
##    xx=random.randint(-250,250)
##    yy=random.randint(-250,250)
##    pp=random.randint(3,9)
##    p.tracer(False)
##    for l in range(numStars):
##        p.up()
##        p.goto(xx,yy)
##        p.down()
##        star(p,pp,10)
##        xx=random.randint(-250,250)
##        yy=random.randint(-250,250)
##        pp=random.randint(3,9)
##    p.tracer(True)
##a=random.randint(1,50)
##sky(200)
##
