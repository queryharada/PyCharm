# -*- coding:utf-8 -*-

def sumDigits(s):
    try:
        total = 0
        for c in s:
            total += int(c)
        return total

    except ValueError:
        print(c, 'is not an integer ')
        return -1


if __name__ == "__main__":
    print(sumDigits('12345'))
    print(sumDigits('123a45'))
    pass
