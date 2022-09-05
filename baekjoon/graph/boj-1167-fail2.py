# 1167. 트리의 지름
## 나름 깔끔하다 생각했는데 이것도 시간초과라니...

from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(v, l, visited=None):
    if visited is None:
        visited = []

    visited.append(v)

    for w in graph[v]:
        node, cost = w
        if node not in visited:
            distance[node] = l + cost
            dfs(node, l + cost, visited)


# 트리의 정점의 개수
V = int(input())

# 간선 정보 저장
graph = defaultdict(list)
for _ in range(V):
    inputs = list(map(int, input().split()))
    a = inputs[0]

    for i in range(1, len(inputs), 2):
        if inputs[i] == -1:
            break
        b, cost = inputs[i], inputs[i + 1]
        graph[a].append((b, cost))


# DFS 1: 임의의 정점(1)에서 가장 거리가 먼 정점 구하기
distance = [-1] * (V + 1)
dfs(1, 0)
max_node = distance.index(max(distance))

# DFS 2: 가장 거리가 먼 정점에서 최대 거리인 정점 구하기
distance = [-1] * (V + 1)
dfs(max_node, 0)

print(max(distance))