# -*- coding:utf-8 -*-

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = 10
    for i in range(n + 1):
        print('bib of', i, '=', fib(i))
