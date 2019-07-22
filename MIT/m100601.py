# -*- coding:utf-8 -*-

class intDict(object):
    def __init__(self, numBuckets):
        self.buckets = list()
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, key, dictVal):
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))

    def getValue(self, key):
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'


if __name__ == "__main__":
    import random

    D = intDict(17)
    for i in range(20):
        key = random.choice(range(10 ** 5))
        D.addEntry(key, i)

    print('The value of the intDict is:')
    print(D)
    print('\n', 'The buckets are:')
    for hashBucket in D.buckets:
        print('   ', hashBucket)

