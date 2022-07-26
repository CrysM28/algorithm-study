# 트리의 지름
from collections import defaultdict
import sys

# 재귀
sys.setrecursionlimit(10**9)
def dfs(v, l):
    for node, cost in tree[v]:
        if distance[node] == -1:
            distance[node] = l + cost
            dfs(node, l + cost)

# 스택
def dfs(start_v):
    distance = [-1] * (N + 1)
    stack = [(start_v,0)]

    while stack:
        v, l = stack.pop()
        for node, cost in tree[v]:
            if distance[node] == -1:
                stack.append((node, l + cost))
        distance[v] = max(distance[v], l)
    return distance



# 입력: V개의 정점, tree
V = int(input())
tree = defaultdict(list)
for _ in range(V-1):
    a, b, cost = list(map(int, input().split()))
    tree[a].append((b, cost))
    tree[b].append((a, cost))

# DFS 1: 임의의 정점(1)에서 가장 거리가 먼 정점 구하기
distance = [-1] * (V + 1)
distance[1] = 0
dfs(1, 0)
max_node = distance.index(max(distance))

# DFS 2: 가장 거리가 먼 정점에서 최대 거리인 정점 구하기
distance = [-1] * (V + 1)
distance[max_node] = 0
dfs(max_node, 0)

# 최대값이 거리
print(max(distance))