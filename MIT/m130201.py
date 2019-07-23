# -*- coding:utf-8 -*-
def fastFib(n, memo=dict()):
    if n == 0 or n == 1:
        return 1
    # try:
    #     return memo[n]
    # except KeyError:
    #     result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
    #     memo[n] = result
    #     return result
    if n in memo:
        return memo[n]

    result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
    memo[n] = result
    return result


if __name__ == "__main__":
    print(fastFib(10, memo=dict()))
