# -*- coding:utf-8 -*-
#
#

x = int(input('Enter an integer: '))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
if ans ** 3 != abs(x):
    print(x, 'is not a perfect code ')
else:
    if x < 0:
        ans = -ans
    print('Code root of', x, 'is', ans)
