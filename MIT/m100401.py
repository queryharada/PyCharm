# -*- coding:utf-8 -*-
# O(lenL) x log2(len(L))
def merge(left, right, compare):
    result = list()
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

#
def mergeSort(L, compare=lambda x, y: x < y):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


if __name__ == "__main__":
    list1 = [0.359081995, 0.275002879, 0.009691899, 0.74641451,
             0.097950418, 0.451868028, 0.754008108, 0.821939172,
             0.391127468, 0.692700199, 0.668507531, 0.891516867,
             0.771374075, 0.58466806, 0.753544979, 0.252906854
             ]
    print(mergeSort(list1))
    print(mergeSort(list1, lambda x, y: x > y))
