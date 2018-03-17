#Homework 3 for Jake Hayes
from math import *
import random
#2.18
def wallis(pairs):
    acc=1.0
    num=2.0
    for apair in range(pairs):
        leftterm=num/(num-1)
        rightterm=num/(num+1)
        acc=acc*leftterm*rightterm
        num=num+2
    pi=acc*2
    return pi
print(wallis(10000))
print(wallis(100000))
#2.19
def archimedes(numsides):
    innerangleB=360/numsides
    halfangleA=innerangleB/2
    onehalfsideS=sin(radians(halfangleA))
    sideS=onehalfsideS*2
    polygonCircumference=numsides*sideS
    pi=polygonCircumference/2
    return pi
def leibniz(terms):
    acc=0
    num=4
    den=1
    for aterm in range(terms):
        nextterm=num/den*(-1)**aterm
        acc=acc+nextterm
        den=den+2
    return (acc)
print(wallis(10000))
print(archimedes(10000))
print(leibniz(10000))
#2.20
def wallis2(pairs):
    acc=1.0
    num=2.0
    for apair in range(pairs):
        leftterm=num/(num-1)
        rightterm=num/(num+1)
        acc=acc*leftterm*rightterm
        num=num+2
    pi=acc*2
    return pi
print(wallis2(1000))
#2.21
print("The expression is either true or false.")
#2.22
print("There must be two expressions because a bool can not be true and false.")
#2.23
print("not 7>3 should come up as an error.")
#2.24
print("Nothing will pass because it is either true or false, nothing else.")
#2.25
print("There must be two bools or this expression will not work.")
#2.26
print("There must have been an error in assigning the boolean expression.")
#2.27
print("if i<10 and i>1: bool(true)")
#2.28
print("Python will know which else goes to which if based on indentation.")
#2.29
def question(result):
    answer=2
    if result==100:
        answer=1
    else:
        answer=2
    return answer
print(question(100))
#2.30
def gpa1(score):
    if score>=90:
        gradepoint=4
    else:
        if score>=80:
            gradepoint=3
        else:
            if score>=70:
                gradepoint=2
            else:
                if score>=60:
                    gradepoint=1
                else:
                    gradepoint=0
    return gradepoint
print(gpa1(random.randint(1,100)))
#2.31
def gpa(score):
    if score>=90:
        gradepoint=4
    elif score>=80:
        gradepoint=3
    elif score>=70:
        gradepoint=2
    elif score>=60:
        gradepoint=1
    else:
        gradepoint=0
    return gradepoint
print(gpa(random.randint(1,100)))
#2.32
def findLeap(year):
    test=year%4
    test1=year%4
    if test==0:
        if test1==0:
            return(True)
        else:
            return(False)
    else:
        return(False)
print(findLeap(2012))
#2.33
def cost(pounds):
    price=7.50+(.32*pounds)
    if pounds>100:
        price=price-1.50
    return(price)
print(cost(1))
#2.34
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>b and c>a:
        return c
    else:
        return("Invalid entry")
print(largest(1,3,2))
#2.35
def paycheck(rate,hours):
    if hours<=40:
        pay=rate*hours
    else:
        ot=hours-40
        otrate=rate*1.5
        otpay=ot*otrate
        hours=hours-ot
        pay=(rate*hours)+(otpay)
    return pay
print(paycheck(5,42))
