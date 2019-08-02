# -*- coding:utf-8 -*-
import pylab
import random


def variance(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    return variance(X) ** 0.5


def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)


def flipPlot1(minExp, maxExp, numTrials):
    ratiosMeans, diffMeans, ratiosSDs, diffsSDs = list(), list(), list(), list()
    xAxis = list()
    for exp in range(minExp, maxExp - 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = list(), list()
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString = '(' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratis ' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips ',
             'Mean Heads/Tails ', 'ko', logX=True)
    title = 'SD Heads/Tails Ratis ' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of flips ',
             'Standard Devision ', 'ko', logX=True, logY=True)

    pylab.show()


if __name__ == "__main__":
    flipPlot1(4, 20, 20)
