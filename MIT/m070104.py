# -*- coding:utf-8 -*-

def getRatios(vect1, vect2):
    ratios = list()
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index] / vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))  # nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

if __name__ == "__main__":

    try:
        vect1 = [1, 2, 3, 4, 5, 6]
        vect2 = [6, 7, 8, 9, 10, 11]
        print(getRatios(vect1, vect2))

        vect1 = [1, 2, 3, 4, 5, 6]
        vect2 = [6, 0, 8, 9, 10, 11]
        print(getRatios(vect1, vect2))

        vect1 = []
        vect2 = []
        print(getRatios(vect1, vect2))

        vect1 = [1, 'a', 3, 4, 5, 6]
        vect2 = [6, 7, 8, 9, 10, 11]
        print(getRatios(vect1, vect2))

        # 以降は実行されない
        vect1 = [1, 2, 3, 4, 5, 6]
        vect2 = [6, 7, 8, 9, 10]
        print(getRatios(vect1, vect2))

    except ValueError as msg:
        print(msg)
