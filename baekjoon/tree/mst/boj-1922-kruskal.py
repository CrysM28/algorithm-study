# 1922. 네트워크 연결
## 크루스칼로 풀이 -> PyPy3: 524 ms
from collections import defaultdict

V = int(input())
E = int(input())

# 부모 초기화
parent = defaultdict(int)
for i in range(1, V + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    # 같은 집합이면 사이클 발생
    if a == b:
        return True

    # 다른 집합이면 더 작은 쪽을 부모로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False


edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort() 

total_cost = 0
for edge in edges:
    cost, a, b = edge

    # 사이클 발생하지 않으면 MST에 포함
    if not union(a, b):
        total_cost += cost

print(total_cost)
