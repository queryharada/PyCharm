# -*- coding:utf-8 -*-

total = 0
a = '1.23,2.4,3.123'
for c in a:
    if c.isnumeric():
        total = total + int(c)
print(total)
