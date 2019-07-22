# -*- coding:utf-8 -*-

def isPal(x):
    temp = x[:] # deep copy
    temp.reverse()
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = list()
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    silly(5)
