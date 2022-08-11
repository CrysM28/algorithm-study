# 11050. 이항 계수 1

from itertools import combinations as c
n, k = map(int, input().split())
a = len(list(c(range(n),k)))
print(a)
