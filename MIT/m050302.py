# -*- coding:utf-8 -*-

L = [x ** 2 for x in range(1, 7)]
print(L)

mixed = [1, 2, 'a', 3, 4.]
print([x ** 2 for x in mixed if type(x) == int])
