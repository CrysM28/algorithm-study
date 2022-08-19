# 15650. N과 M (2)
from itertools import combinations

N, M = map(int, input().split())
n = range(1, N+1)

a = combinations(n, M)

for aa in a:
    print(*aa)

