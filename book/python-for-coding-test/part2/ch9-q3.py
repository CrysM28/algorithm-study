# 전보
from collections import defaultdict
import heapq

def dijkstra(start):
    # 최단거리 배열
    dist = defaultdict(int)

    # 우선순위 큐
    unvisited = [(0, start)]

    while unvisited:
        time, node = heapq.heappop(unvisited)

        if node not in dist:
            dist[node] = time
            
            # 인접 노드 추가
            for v, w in graph[node]:
                alt = w + time
                heapq.heappush(unvisited, (alt, v))

    return dist


# 도시 수, 통로 수, 출발 도시
n, m, c = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 받을 수 있는 도시 수, 총 걸리는 시간
ans = dijkstra(c)
print(len(ans)-1, max(ans.values()))
