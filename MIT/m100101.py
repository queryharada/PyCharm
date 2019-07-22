# -*- coding:utf-8 -*-
# O(len(L))
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False


def search2(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# O(log(len(L)))
def search3(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else: # L[mid] > e
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


if __name__ == "__main__":
    print(search(['AAAA', 'BBBB', 'CCCC'], 'CCCC'))
    print(search(['AAAA', 'BBBB', 'CCCC'], 'DDDD'))
    list1 = ['CCCC', 'BBBB', 'AAAA']
    list1.sort()
    print(search2(list1, '0000'))
    list1 = [0.359081995, 0.275002879, 0.009691899, 0.74641451,
             0.097950418, 0.451868028, 0.754008108, 0.821939172,
             0.391127468, 0.692700199, 0.668507531, 0.891516867,
             0.771374075, 0.58466806, 0.753544979, 0.252906854
             ]
    # sort(): 元のリストをソート、リスト型のメソッド
    # sorted(): ソートした新たなリストを生成、組み込み関数
    list1.sort()
    # O(sortComplexity(L))      amortize:償却する
    print(search3(list1, 0.692700199))
    print(search3(list1, 0.6))
