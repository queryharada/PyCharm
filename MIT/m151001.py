import random
import pylab


def squareRoot(x, epsilon):
    pass


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def variance(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    return variance(X) ** 0.5


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
    return heads / float(numFlips)


def flipSim(numFlpsPerTrial, numTrials):
    fracHeads = list()
    for i in range(numTrials):
        fracHeads.append(flip(numFlpsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)


def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads ')
    pylab.ylabel('Number of Trials ')
    pylab.annotate('Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)),
                   size='x-large ', xycoords='axes fraction ', xy=(0.67, 0.5))


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()

    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val1, bins=20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)


if __name__ == "__main__":
    makePlots(100, 1000, 100000)
