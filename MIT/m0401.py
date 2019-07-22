# -*- coding:utf-8 -*-

def includeStr(srcString, incString):
    return incString in srcString


if __name__ == "__main__":
    srcString = 'abcdefghijk'
    incString = 'ijka'

    print(includeStr(srcString, incString))
