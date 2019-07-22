# -*- coding:utf-8 -*-

x = 25
epssilon = 0.01
step = epssilon ** 2
numGuesses = 0
ans = 0.0
while abs(ans ** 2 - x) >= epssilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans ** 2 - x) >= epssilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)

#
#
#
x = 25
epssilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epssilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print('numGuesses =', numGuesses)
if abs(ans ** 2 - x) >= epssilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)
