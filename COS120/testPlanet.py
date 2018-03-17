import planetClass

def createSomePlanets():
    aPlanet=planetClass.Planet("Zorks",2000,30000,100000,5)
    bPlanet=planetClass.Planet("Zapps",1000,20000,200000,17)
    print(aPlanet.getName() + " has a radius of " + str(aPlanet.getRadius()))
    planetList=[aPlanet,bPlanet]
    for planet in planetList:
        print(planet.getName() + " has a mass of " + str(planet.getMass()))
    for planet in planetList:
        print(planet.getName() + " has " + str(planet.getMoons()) + " moons.")
    print(bPlanet.getName() + " has a circumference of " + str(bPlanet.getCircumference()))

createSomePlanets()
