# 1753. 최단경로

from collections import defaultdict
from heapq import heappush, heappop
import sys

INF = sys.maxsize


def dijkstra(start):
    dist = [INF for _ in range(V + 1)]
    dist[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        time, node = heappop(unvisited)
        if dist[node] < time:
            continue
        for v, w in graph[node]:
            alt = time + w
            if dist[v] > alt:
                dist[v] = alt
                heappush(unvisited, (alt, v))

    return dist


V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for d in dijkstra(start)[1:]:
    if d == INF: print("INF")
    else: print(d)