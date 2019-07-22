# -*- coding:utf-8 -*-
# x**2 - 24 = 0 で 誤差が epsilon 以下になる x を求める
epsilon = 0.01
k = 24.0
guess = k / 2.0

while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))

print('Square root of', k, 'is about', guess)
