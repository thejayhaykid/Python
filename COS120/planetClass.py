import math
class Planet:
    def __init__(self, iname, iradius, imass, idistance, imoons): 
        self.name = iname
        self.radius = iradius
        self.mass = imass
        self.distance = idistance
        self.numMoons = imoons

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

    def getCircumference(self):
        c = 2 * math.pi * self.radius
        return c
