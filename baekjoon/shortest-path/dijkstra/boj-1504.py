# 1504. 특정한 최단 경로
from collections import defaultdict
from heapq import heappush, heappop

INF = int(10e9)

def dijkstra(start):
    dist = [INF for _ in range(N+1)]  # 노드별 최단경로 저장 (dist[node] = time)
    dist[start] = 0
    Q = [(0, start)]  # (time, node)

    while Q:
        time, node = heappop(Q)   
        for v, w in graph[node]:
            alt = time + w
            if dist[v] == 0 or dist[v] > alt:
                dist[v] = alt
                heappush(Q, (alt, v))
    dist[start] = 0
    return dist


# 정점, 간선
N, E = map(int, input().split())

# 그래프를 인접 리스트 형태로 저장
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))     # 양방향 길

# 반드시 지나야 하는 정점 2개
v1, v2 = map(int, input().split())


d_1 = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)
d_N = dijkstra(N)

# path1: 1 - v1 - v2 - N
path1 = d_1[v1] + d_v1[v2] + d_v2[N]
# path2: 1 - v2 - v1 - N
path2 = d_1[v2] + d_v2[v1] + d_v1[N]

min_path = min(path1, path2)
print(min_path if min_path < INF else -1)



