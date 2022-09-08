# 1238. 파티
from collections import defaultdict
from heapq import heappop, heappush
import sys

INF = sys.maxsize

def dijkstra(start):
    dist = defaultdict(int)
    unvisited = [(0, start)]

    while unvisited:
        time, node = heappop(unvisited)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heappush(unvisited, (alt, v))

    if len(dist) != V:
        for i in range(1, V + 1):
            if i not in dist:
                dist[i] = INF

    return dist


# 정점, 간선, 마을
V, E, X = map(int, input().split())

# 그래프
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# x까지의 거리
distance_x = defaultdict(int)

for i in range(1, V+1):
    dist = dijkstra(i)
    distance_x[i] += dist[X]
    if i == X:
        for j in range(1, V+1):
            distance_x[j] += dist[j]

vals = distance_x.values()
ans = max(vals)

print(ans)