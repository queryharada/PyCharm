# -*- coding:utf-8 -*-
import pylab

if __name__ == "__main__":
    # pylab.figure(1)
    # pylab.plot([1, 2, 3, 4], [1, 7, 3, 5])
    # pylab.show()

    # pylab.figure(1)
    # pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])
    # pylab.figure(2)
    # pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])
    # pylab.savefig('Figure-Addie')
    # pylab.figure(1)
    # pylab.plot([5, 6, 10, 3])
    # pylab.savefig('Figure-Jane')

    principal = 10000
    interestRate = 0.05
    years = 20
    values = list()
    for i in range(years +1):
        values.append(principal)
        principal += principal *interestRate
    pylab.plot(values, 'ko')
    pylab.title('5% Groth, Compounded Annually ')
    pylab.xlabel('Years of Compounding ')
    pylab.ylabel('Value of Principal ($) ')
    pylab.show()