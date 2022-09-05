# 1167. 트리의 지름
from collections import defaultdict


def dfs(v, l):
    global max_weight
    global max_node

    visited.append(v)
    for w in graph[v]:
        if w[0] not in visited:
            cur_max = dfs(w[0], l + w[1])       # 트리의 한 가지에 대해 dfs
            max_weight = max(cur_max[1], max_weight)     # 최대값 트랙킹
            if max_weight == cur_max[1]:
                max_node = cur_max[0]       # 가장 먼 노드값 저장
    return v, l


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

visited = []
max_weight = 0
max_node = 0

# DFS 1: 임의의 정점(1)에서 가장 거리가 먼 정점 구하기
dfs(1, 0)

# DFS 2: 가장 거리가 먼 정점에서 최대 거리인 정점 구하기
visited = []
cur_max = 0
dfs(max_node, 0)

print(max_weight)