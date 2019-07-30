# -*- coding:utf-8 -*-
import random
import pylab


def squareRoot(x, epsilon):
    pass


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / numFlips


def flipSim(numFlpsPerTrial, numTrials):
    fracHeads = list()
    for i in range(numTrials):
        fracHeads.append(flip(numFlpsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    return mean


def regressToMean(numFlips, numTrials):
    fracHeads = list()
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    extreams, nextTrials = list(), list()
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extreams.append(fracHeads[i])
            nextTrials.append(fracHeads[i + 1])

    pylab.plot(range(len(extreams)), extreams, 'ko',
               label='Extream')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^',
               label='Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extreams) + 1)
    pylab.xlabel('Extream Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc='best')
    pylab.show()


def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = list(), list(), list()
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTrails = numFlips - numHeads
        try:
            ratios.append(numHeads / numTrails)
            diffs.append(abs(numHeads - numTrails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails ')
    pylab.xlabel('Number of Flips ')
    pylab.ylabel('Abs(#Heads - #Tails ')
    pylab.plot(xAxis, diffs, 'k')
    pylab.figure()

    pylab.title('Head/Tails Ratios ')
    pylab.xlabel('Number of Flips ')
    pylab.ylabel('#Heads/#Tails ')
    pylab.plot(xAxis, ratios, 'k')

    pylab.show()


if __name__ == "__main__":
    # rollN(10)
    # print('Mean =', flipSim(2, 1))
    # print('Mean =', flipSim(10, 1))
    # print('Mean =', flipSim(10, 1))
    # print('Mean =', flipSim(10, 100))
    # print('Mean =', flipSim(10, 100))
    # print('Mean =', flipSim(100, 100000))
    # print('Mean =', flipSim(100, 100000))

    # regressToMean(15, 40)

    random.seed(0)
    flipPlot(4, 20)
