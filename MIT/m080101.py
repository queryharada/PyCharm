# -*- coding:utf-8 -*-


class IntSet(object):
    def __init__(self):
        self.vals = list()

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found ')

    def getMembers(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}'

    def __eq__(self, other):
        if isinstance(other, IntSet):
            return self.vals == other.vals
        return False

if __name__ == "__main__":

    s = IntSet()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    print(type(IntSet), type(IntSet.insert))
    print(s.member(3))
    print(s.getMembers())
    print(s)

    s2 = IntSet()
    s2.insert(1)
    s2.insert(2)
    s2.insert(3)
    s2.insert(4)

    s3 = s
    try:
        assert s == s2, 's == s2'
        assert s == 2, 's == 2'

    except AssertionError as errorMsg:
        print('AssertionError :', errorMsg)
