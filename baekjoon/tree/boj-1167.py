# 1167. 트리의 지름
from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(v, l):
    for node, cost in graph[v]:
        if distance[node] == -1:
            distance[node] = l + cost
            dfs(node, l + cost)


# 트리의 정점의 개수
V = int(input())

# 간선 정보 저장
graph = defaultdict(list)
for _ in range(V):
    inputs = list(map(int, input().split()))
    a = inputs[0]
    for i in range(1, len(inputs) - 2, 2):
        b, cost = inputs[i], inputs[i + 1]
        graph[a].append((b, cost))


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