# -*- coding:utf-8 -*-

numSuccesses = 4
numFailures = 0

try:
    successFailureRatio = numSuccesses / numFailures
    print('The success/failure ratio is ', successFailureRatio)
except ZeroDivisionError:
    print('No failures , so the success ratio is undefined.')
print('Now here')
