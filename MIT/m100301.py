# -*- coding:utf-8 -*-
# O(lenL)**2
def selSort(L):
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    return L


if __name__ == "__main__":
    list1 = [0.359081995, 0.275002879, 0.009691899, 0.74641451,
             0.097950418, 0.451868028, 0.754008108, 0.821939172,
             0.391127468, 0.692700199, 0.668507531, 0.891516867,
             0.771374075, 0.58466806, 0.753544979, 0.252906854
             ]
    print(selSort(list1))
