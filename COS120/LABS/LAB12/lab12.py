import math
#L12-01
class Planet:
    def __init__(self, iname, iradius, imass, idistance, imoons, moonList): 
        self.name = iname
        self.radius = iradius
        self.mass = imass
        self.distance = idistance
        self.numMoons = imoons
        self.listMoons = moonList

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getMoons(self):
        return self.numMoons

    def setMoons(self):
        self.numMoons = input("Enter new number for moons =>")

    def getCircumference(self):
        c = 2 * math.pi * self.radius
        return c

    def getMoonList(self):
        return self.listMoons
    
    def addMoon(self):
        newMoon = input("Enter a name for new moon =>")
        self.listMoons.append(newMoon)

#L12-02
class Sentence:
    def __init__(self, aString):
        self.sentence = aString
        wordList = aString.split()
        self.listWords = wordList

    def getSentence(self):
        return self.sentence

    def getWords(self):
        return self.listWords

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.listWords)

    def capSentence(self):
        self.sentence = self.sentence.upper()
        return self.sentence

    def addPunctuation(self):
        pMark = input("Enter puncctuatuion mark to add to end =>")
        self.sentence = self.sentence + pMark
        return self.sentence

#L12-03
class Sentence2:
    def __init__(self, aString):
        self.sentence = aString
        self.list = []
        self.list.append(aString)

    def getList(self):
        return self.list

    def getSentence(self):
        return self.sentence

    def getWords(self):
        return self.sentence.split()

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.sentence.split())

#L12-04
#10.8 & 10.9 is in class Planet:
#10.10 & 10.11 is in class Sentence:


#L12-05  
class Time:
    def __init__(self,hours,minutes,seconds):
        if hours>23 or hours<0:
            hours=0
        if minutes>59 or minutes<0:
            minutes=0
        if seconds>59 or seconds<0:
            seconds=0
        self.hour = hours
        self.minute = minutes
        self.second = seconds

#L12-06
    def getTime(self):
        if self.hour < 10:
            pre = '0'
        else:
            pre = ''
        if self.minute < 10:
            pre2 = '0'
        else:
            pre2 = ''
        if self.second < 10:
            pre3 = '0'
        else:
            pre3 = ''
        print(pre + str(self.hour) + ":" + pre2 + str(self.minute) + ":" + pre3 + str(self.second))

#L12-07
    def addSec(self):
        self.second = self.second + 1
        if self.second > 59:
            self.second = 0

    def subSec(self):
        self.second = self.second - 1
        if self.second < 0:
            self.second = 59

#L12-08
    def showHour(self):
        return self.hour

    def showMinute(self):
        return self.minute

    def showSecond(self):
        return self.second

#L12-09
    def changeHour(self):
        newHour = int(input("Enter the hour you would like =>"))
        if newHour > 23 or newHour < 0:
            return -1
        else:
            self.hour = newHour
            return

    def changeMinute(self):
        newMinute = int(input("Enter the minute you would like =>"))
        if newMinute > 59 or newMinute < 0:
            return -1
        else:
            self.minute = newMinute
            return

    def changeSecond(self):
        newSecond = int(input("Enter the second you would like =>"))
        if newSecond > 59 or newSecond < 0:
            return -1
        else:
            self.second = newSecond
            return

#L12-10
    def convertToSec(self):
        Seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return Seconds

    def differenceInTime(self, time2):
        time1 = self.convertToSec()
        time2 = time2.convertToSec()
        if time1 > time2:
            difference = time1 - time2
        else:
            difference = time2 - time1
        return difference

#L12-11
    def addTime(self):
        addHour = int(input("Enter number of hours to add =>"))
        addMinute = int(input("Enter number of minutes to add =>"))
        addSecond = int(input("Enter number of seconds to add =>"))
        for anHour in range(addHour):
            self.hour+=1
            if self.hour>23:
                self.hour=0
        for aMinute in range(addMinute):
            self.minute+=1
            if self.minute>59:
                self.minute=0
        for aSec in range(addSecond):
            self.second+=1
            if self.second>59:
                self.second=0

#L12-12
    def fullDay(self):
        for i in range(3600*24):
            self.addSec()
            if self.second == 0:
                self.minute+=1
            if self.minute>59:
                self.minute=0
                self.hour+=1
            if self.hour>23:
                self.hour=0
            self.getTime()
                
