# 11779. 최소비용 구하기 2
from collections import defaultdict
import heapq as h


INF = int(1e9)

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


## dijkstra
start, end = map(int, input().split())

# start부터의 거리
dist = [INF] * (n+1)
dist[start] = 0

# 이전에 방문한 노드
visited = [INF] * (n+1)
visited[start] = 0

# (time, node)
unvisited = [(0, start)]

while unvisited:
    time, node = h.heappop(unvisited)

    if dist[node] < time:
        continue

    for v,w in graph[node]:
        t = time+w
        if dist[v] > t:
            dist[v] = t
            h.heappush(unvisited, (t, v))
            visited[v] = node

## 역추적
ans = []
node = end
while node != 0:
    ans.append(node)
    node = visited[node]

# answers
print(dist[end])
print(len(ans))
print(*ans[::-1])