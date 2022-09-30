# 13016. 내 왼손에는 흑염룡이 잠들어 있다

from collections import defaultdict

# 국가의 수 (정점)
N = int(input())

# 도로 정보 (간선)
graph = defaultdict(list)
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


# 트리의 지름 찾기와 같은 논리
def dfs(start_v):
    distance = [-1] * (N + 1)
    stack = [(start_v, 0)]

    while stack:
        v, l = stack.pop()
        for node, cost in graph[v]:
            if distance[node] == -1:
                stack.append((node, l + cost))
        distance[v] = max(distance[v], l)
    return distance


# DFS 1: 1에서 최대 거리인 정점 구하기 -> 단말 정점 1: u
distance = dfs(1)
u = distance.index(max(distance))

# DFS 2: u에서 최대 거리인 정점 구하기 -> 단말 정점 2: v
u_dist = dfs(u)
v = u_dist.index(max(u_dist))

# DFS 3: v에서 최대 거리 구하기
v_dist = dfs(v)


# 단말 노드인 u, v와의 거리 중 최대인 것이 정답
for i in range(1, N + 1):
    print(max(u_dist[i], v_dist[i]))
