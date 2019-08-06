# -*- coding:utf-8 -*-
import random
import pylab

vals = list()
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins=10)
pylab.ylabel('Number of Occurrences ')

pylab.show()
