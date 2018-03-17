#Lab 03 for Jake Hayes 9/18/2012
#L03-1
from math import *
from random import *
def demoCalls():
  sqrt(16)
  print(sqrt(16))
  x=sqrt(16)
  print(x)
  y=sqrt(16) * sqrt(25)
  print(y)
##demoCalls()
def mySQRT(n,iters):
  X=1
  for i in range(iters):
    X=1/2*(X+n/X)
  return(X)
def testmySQRT():
  mySQRT(16,100)
  print(mySQRT(16,100))
  x= mySQRT(16,100)
  print(x)
  y= mySQRT(16,100) * mySQRT (25,100)
  print(y)
##testmySQRT()
#L03-2
##for i in range(3):
##    print("in the loop")
##for l in range(1):
##    print("in the loop")
##    print("in the loop")
##    print("in the loop")
##for j in range(5):
##    if j < 3:
##        print("in the loop")
##count=1
##for k in range(5):
##    if count <= 3:
##        print("in the loop")
##        count=count+1
##for m in range(-1,2):
##    print("in the loop")
##for n in range(-5,-2):
##    print("in the loop")
#L03-3
def schoolDaze(age):
  if age<1 or age>18:
    print("Invalid Entry")
  if age>=14 and age<=18:
    print("High School")
  if age>=12 and age<=13:
    print("Middle School")
  if age>=6 and age<=11:
    print("Elementary School")
  if age>=4 and age<=5:
    print("Preschool")
  if age>=1 and age<=3:
    print("Nursery")
##schoolDaze(randint(1,20))
#L03-4
def schoolDaze0(age):
  if age<1 or age>18:
    print("Invalid Entry")
  else:
    if age>=14:
      print("High School")
    else:
      if age>=12:
        print("Middle School")
      else:
        if age>=6:
          print("Elementary School")
        else:
          if age>=4:
            print("Preschool")
          else:
            print("Nursery")
##schoolDaze0(17)
#L03-5
def schoolDaze(age):
  if age>=14 and age<=18:
    print("High School")
  elif age>=12:
    print("Middle School")
  elif age>=6:
    print("Elementary School")
  elif age>=4:
    print("Preschool")
  elif age>=1:
    print("Nursery")
  else:
    print("Invalid Entry")
  return(0)
##schoolDaze(randint(1,20))
#L03-6
def PRS(p1,p2):
  if p1=="rock" and p2=="scissors":
    print("rock dulls scissors, p1 wins")
  elif p1=="scissors" and p2=="paper":
    print("scissors cuts paper, p1 wins")
  elif p1=="paper" and p2=="rock":
    print("paper covers rock, p1 wins")
  elif p2=="rock" and p1=="scissors":
    print("rock dulls scissors, p2 wins")
  elif p2=="scissors" and p1=="paper":
    print("scissors cuts paper, p2 wins")
  elif p2=="paper" and p1=="rock":
    print("paper covers rock, p2 wins")
  elif p1==p2:
    print("TIE!")
  else:
    print("Invalid Entry")
##PRS("rock","scissors")
#L03-7
def testPRS():
  for q in range(10):
    randp1=randint(1,3)
    randp2=randint(1,3)
    if randp1==1:
      p1play="rock"
    elif randp1==2:
      p1play="paper"
    else:
      p1play="scissors"
    if randp2==1:
      p2play="rock"
    elif randp2==2:
      p2play="paper"
    else:
      p2play="scissors"
    PRS(p1play,p2play)
##testPRS()
#L03-8
def calcAutoPremium(age,numDoors,gender):
  if age<21:
    if numDoors==2:
      print ("High Risk")
      premium=2500
      if gender=="female":
          premium=premium*(2/3)
          print("female")
      else:
                            premium=premium*2
                            print("male")
    else:
      print ("Semi-High Risk")
      premium=1900
      if gender=="female":
                            premium=premium*(2/3)
                            print("female")
      else:
                            premium=premium*2
                            print("male")

      
  else:
    if numDoors==2:
      print ("Medium Risk")
      premium=1500
    else:
      print ("Low Risk")
      premium=800
  monthlyPayment=premium/12.0
  return monthlyPayment
##print(calcAutoPremium(18,4,"male"))
#L03-9
def testAutoPremium():
    for i in range(10):
        if randint(1,2)==1:
            gender="male"
        else:
            gender="female"
        doors=randint(2,4)
        age=randint(16,28)
        for p in range(3):
            print(calcAutoPremium(age,doors,gender))
##testAutoPremium()
#L03-10
def stringThing():
    first="Jacob "
    middle="Jeffrey "
    last="Hayes"
    full="Jacob Jeffrey Hayes"
    print(full)
    print(full[0:5])
    print(full[14:20])
    print(full[14:20]+", "+full[0:5])
    print(len(full[0:5]))
    s="s"
    p="p"
    print("mi"+s*2+"i"+s*2+"i"+p*2+"i")
    m="mississippi"
    name="Roy G Biv"
    for i in range(len(name)+1):
        print(name[0:i])
    print(m.count(s))
    print(m.replace("iss","ox"))
    m.replace("iss","ox")
    print(m.index("p"))
    astring="python"
    print(astring.center(20))
    astring=astring.upper()
    print(astring.center(20))
stringThing()
