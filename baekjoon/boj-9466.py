# 9466. 텀 프로젝트

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    parent = [i for i in range(n+1)]
    student = [0] + [arr[i] for i in range(n)]

    for i in range(1, n+1):
        union(i, student[i])

    print(parent)