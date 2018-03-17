import lab12

def createSomePlanets():
    aPlanet=lab12.Planet("Zorks",2000,30000,100000,5,['Steve','Lou','The Grinch'])
    bPlanet=lab12.Planet("Zapps",1000,20000,200000,17,[])
    print(aPlanet.getName() + " has a radius of " + str(aPlanet.getRadius()))
    planetList=[aPlanet,bPlanet]
    for planet in planetList:
        print(planet.getName() + " has a mass of " + str(planet.getMass()))
    for planet in planetList:
        print(planet.getName() + " has " + str(planet.getMoons()) + " moons.")
    print(bPlanet.getName() + " has a circumference of " + str(bPlanet.getCircumference()))
    aPlanet.setMoons()
    print(aPlanet.getName() + " has " + str(aPlanet.getMoons()) + " moons.")
    aPlanet.addMoon()
    print("The list of moons for " + aPlanet.getName() + " is " + str(aPlanet.getMoonList()))
 

##createSomePlanets()


def makeASentence():
    aString = "The quick brown fox jumps over the lazy dog"
    aSentence = lab12.Sentence(aString)
    print(aSentence.getSentence())
    print(aSentence.getWords())
    print(aSentence.getLength())
    print(aSentence.getNumWords())
    print(aSentence.capSentence())
    print(aSentence.addPunctuation())

##makeASentence()
    
def makeASentence2():
    aString = "The quick brown fox jumps over the lazy dog"
    aSentence = lab12.Sentence2(aString)
    print(aSentence.getList())
    print(aSentence.getSentence())
    print(aSentence.getWords())
    print(aSentence.getLength())
    print(aSentence.getNumWords())

##makeASentence2()

def Time():
    myTime = lab12.Time(15,25,59)
    myTime2 = lab12.Time(6,8,0)
##    myTime.getTime()
##    myTime2.getTime()
##    myTime.addSec()
##    myTime2.subSec()
##    myTime.getTime()
##    myTime2.getTime()
##    print(str(myTime.showHour()))
##    print(str(myTime.showMinute()))
##    print(str(myTime.showSecond()))
##    myTime.changeHour()
##    myTime.changeMinute()
##    myTime.changeSecond()
##    myTime.getTime()
##    print(str(myTime.differenceInTime(myTime2)))
##    myTime.addTime()
##    myTime.getTime()
    myTime.fullDay()

Time()
