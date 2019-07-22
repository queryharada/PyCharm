# -*- coding:utf-8 -*-
from m100401 import *


def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:
        return arg1[0] < arg2[0]


def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:
        return arg1[1] < arg2[1]


if __name__ == "__main__":
    L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
    newL = mergeSort(L, lastNameFirstName)
    print('Sorted by last name=', newL)
    newL = mergeSort(L, firstNameLastName)
    print('Sorted by first name=', newL)

    L = [3, 5, 2]
    D = {'a': 12, 'c': 5, 'b': 'dog'}
    print(sorted(L))
    print(L)
    L.sort()
    print(L)
    print(sorted(D))
    # D.sort()
    L = [[1, 2, 3], (3, 2, 1, 0), 'abc']
    # key=xxx   stable sort
    print(sorted(L, key=len, reverse=True))
