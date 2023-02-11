# 11779. 최소비용 구하기 2
## 예전에 풀다가 말았나봄

from collections import defaultdict
from heapq import heappop, heappush
import sys

INF = sys.maxsize


def dijkstra(start):
    dist = defaultdict(int)
    unvisited = [(0, start)]  
    discovered = []

    while unvisited:
        time, node = heappop(unvisited)
        discovered.append(node)
        
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heappush(unvisited, (alt, v))
                

    if len(dist) != V:
        for i in range(1, V + 1):
            if i not in dist:
                dist[i] = INF

    return dist, discovered

V = int(input())    # 도시 개수
E = int(input())    # 버스 개수

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dist, discovered = dijkstra(start)

print(dist)
print(discovered)