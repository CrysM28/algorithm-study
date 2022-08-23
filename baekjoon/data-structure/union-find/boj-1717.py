# 1717. 집합의 표현
from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = defaultdict(int)
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        if find(a) != find(b):
            union(a, b)
    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")