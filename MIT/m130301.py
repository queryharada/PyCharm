# -*- coding:utf-8 -*-
from MIT.m090301 import *


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + \
                 ', ' + str(self.weight) + '>'
        return result


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = list()
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def fastMaxVal(toConsider, avail, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = fastMaxVal(toConsider[1:],
                                         avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


import random


def smallTest(func):
    name = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weight = [3, 3, 2, 5]
    Items = list()
    for i in range(len(vals)):
        Items.append(Item(name[i], vals[i], weight[i]))
    val, taken = func(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken=', val)


def buildManyItems(numItems, maxVal, maxWeight):
    items = list()
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxWeight)))
    return items


def bigTest(numItems,func):
    items = buildManyItems(numItems, 10, 10)
    val, taken = func(items, 40)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


if __name__ == "__main__":
    smallTest(maxVal)
    bigTest(10,maxVal)
    smallTest(fastMaxVal)
    bigTest(10,fastMaxVal)

