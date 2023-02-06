# 4386. 별자리 만들기
import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    # 사이클 발생
    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True



n = int(input())
parent = [i for i in range(n+1)]
stars = []
edges = []
ans = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append([x, y])

for i in range(n-1):
    for j in range(i+1, n):
        dist = math.sqrt((stars[j][0]-stars[i][0])**2 + (stars[j][1]-stars[i][1])**2)
        edges.append([dist, i, j])

edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클 발생하지 않으면 MST에 추가
    if union(a, b):
        ans += cost

print(round(ans, 2))