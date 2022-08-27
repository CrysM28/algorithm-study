# 11726. 2xn 타일링
## f(n) = f(n-1) + f(n-2)
## 피보나치 DP와 같은 문제

from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
tiles = defaultdict(int)  # 크기가 동적인 0 배열


def fib(n):
    if n <= 2:
        return n

    if tiles[n]:
        return tiles[n]

    tiles[n] = fib(n - 1) + fib(n - 2)
    return tiles[n]


print(fib(N) % 10007)
