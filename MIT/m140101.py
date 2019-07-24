# -*- coding:utf-8 -*-
class Location(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = dict()

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk ')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field ')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field ')
        return self.drunks[drunk]


class oddField(Field):
    def __init__(self, numHoles, xRange, yRange):
        Field.__init__(self)
        self.wormholes = dict()
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


import random


class Drunk(object):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Amonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrails, dClass):
    Homer = dClass()
    origin = Location(0, 0)
    distances = list()
    for t in range(numTrails):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrails, dClass):
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrails, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps ')
        print(' Mean =', round(sum(distances) / len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))


class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def simAll(drunkKinds, walkLengths, numTrails):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrails, dClass)


class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


import pylab


def simDrunk(numTrails, dClass, walkLengths):
    meanDistance = list()
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trails = simWalks(numSteps, numTrails, dClass)
        mean = sum(trails) / len(trails)
        meanDistance.append(mean)
    return meanDistance


def simAll1(drunkKinds, walkLengths, numTrails):
    styleChoice = styleIterator(('m-', 'r:', 'k-'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrails, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
        pylab.title('Mean Distance from Origin ('
                    + str(numTrails) + ' trials)')
        pylab.xlabel('Number of Step')
        pylab.ylabel('Distance of Step')
        pylab.legend(loc='best')
        pylab.semilogx()
        pylab.semilogy()
    pylab.show()


def getFinalLoc(numSteps, numTrails, dClass):
    locs = list()
    d = dClass()
    for t in range(numTrails):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs


def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLoc(numSteps, numTrials, dClass)
        xVals, yVals = list(), list()
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = sum(xVals) / len(xVals)
        meanY = sum(yVals) / len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label=dClass.__name__ + ' mean loc, = <'
                         + str(meanX) + ', ' + str(meanY) + '>')
        pylab.title('Location at End of Walks ('
                    + str(numSteps) + ' steps)')
        pylab.xlabel('Steps East/West of Orign ')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc='lower left')
    pylab.show()


def traceWalk(drunkKinds, numSteps):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    # f = Field()
    f = oddField(1000, 100, 200)
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0, 0))
        locs = list()
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = list(), list()
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label=dClass.__name__)
        pylab.title('Sports Visited on Walk ('
                    + str(numSteps) + ' steps)')
        pylab.xlabel('Steps East/West of Orign ')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc='best')
    pylab.show()


if __name__ == "__main__":
    drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
    drunkTest((0, 1), 100, UsualDrunk)
    simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
    simAll1((UsualDrunk, ColdDrunk, EWDrunk), (10, 100, 1000, 10000), 100)
    plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)
    traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 500)
