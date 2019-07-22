# -*- coding:utf-8 -*-
import copy


class DictSet(object):
    def __init__(self):
        self.vals = dict()

    def insert(self, k, v):
        if not k in self.vals:
            self.vals[k] = v

    def member(self, k):
        if k in self.vals.keys():
            return self.vals[k]
        return k + ' not found '

    def remove(self, k):
        try:
            self.vals.pop(k)
        except:
            raise ValueError(str(k) + ' not found ')

    def getMembers(self):
        return copy.deepcopy(self.vals)

    def __str__(self):
        result = ''
        for k, v in self.vals.items():
            result += k + ':' + str(v) + ','
        return '{' + result[:-1] + '}'

    def __eq__(self, other):
        if isinstance(other, DictSet):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash(self.vals)

if __name__ == "__main__":

    s = DictSet()
    s.insert('A', 1)
    s.insert('B', 2)
    s.insert('C', 3)
    s.insert('D', 4)
    print(type(DictSet), type(DictSet.insert))
    print(s.member('D'))
    print(s.member('E'))
    print(s.getMembers())
    print(s)

    s2 = DictSet()
    s2.insert('A', 1)
    s2.insert('B', 2)
    s2.insert('C', 3)
    s2.insert('D', 4)

    try:
        assert s == s2, 's == s2'
        assert s == 2, 's == 2'

    except AssertionError as errorMsg:
        print('AssertionError : ', errorMsg)
