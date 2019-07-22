# -*- coding:utf-8 -*-

def isPrime(x):
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = 100
    for i in range(n):
        if isPrime(i):
            print(i)
