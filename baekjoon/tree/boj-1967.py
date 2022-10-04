# 트리의 지름
from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(v, l):
    for node, cost in graph[v]:
        if distance[node] == -1:
            distance[node] = l + cost
            dfs(node, l + cost)


V = int(input())
graph = defaultdict(list)
for _ in range(V-1):
    a, b, cost = list(map(int, input().split()))
    graph[a].append((b, cost))
    graph[b].append((a, cost))


# DFS 1: 임의의 정점(1)에서 가장 거리가 먼 정점 구하기
distance = [-1] * (V + 1)
distance[1] = 0
dfs(1, 0)
max_node = distance.index(max(distance))

# DFS 2: 가장 거리가 먼 정점에서 최대 거리인 정점 구하기
distance = [-1] * (V + 1)
distance[max_node] = 0
dfs(max_node, 0)

print(max(distance))