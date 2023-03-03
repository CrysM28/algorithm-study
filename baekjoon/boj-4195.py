# 4195. 친구 네트워크
from collections import defaultdict

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[a] = b


for _ in range(int(input())):
    F = int(input())
    parent = defaultdict()

    for i in range(F):
        a, b = input().split()
        union(a, b)

    print(parent)