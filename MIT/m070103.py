# -*- coding:utf-8 -*-

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return (valType(val))
        except ValueError:
            print(val, errorMsg)

if __name__ == "__main__":
    readVal(int, 'Enter an integer:', 'is not integer')
