# -*- coding:utf-8 -*-
#  O(1)         定数計算時間(constant running time)
#  O(log n)     対数計算時間(logarithmic running time)
def iniToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result


def addDigits(n):
    stringRep = iniToStr(n)
    val = 0
    for c in stringRep:
        val += int(c)
    return val


#  O(n)         線形計算時間      (linear running time)
def addDigits2(s):
    val = 0
    for c in s:
        val += int(c)
    return val


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


#  O(n log n)   対数線形計算時間(log-linear running time)
#  O(n**k)      多項式計算時間(polynominal running time)
def isSubset(L1, L2):
    """O(len(L1) X len(L2))"""
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    """O(len(L1) X len(L2))"""
    tmp = list()
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break

    result = list()
    for e in tmp:
        if e not in result:
            result.append(e)
    return result


# O(c**n)      指数計算時間(exponential running time)
def getBinaryRep(n, numDigits):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enough digits ')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

# O(2**len(L))
def genPowerset(L):
    powerset = list()
    for i in range(0, 2 ** len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = list()
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


if __name__ == "__main__":
    print(iniToStr(1234567))
    print(addDigits(1234567))
    print(addDigits2('1234567'))
    print(factorial(123))
    print(isSubset('12345', '54321'))
    print(isSubset('12345', '5432A'))
    print(intersect('12345', '543254A'))
    print(getBinaryRep(123, 8))
    print(genPowerset([1, 2, 3]))
    print(genPowerset(['A', 'B', 'C', 'D']))
