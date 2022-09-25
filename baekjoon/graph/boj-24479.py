# 24479. 알고리즘 수업 - 깊이 우선 탐색 1

from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline

vertex, edge, start_v = map(int, input().split())

# 인접 리스트
graph = defaultdict(list)
for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


# dfs
count = 1
visited = defaultdict(int)
stack = [start_v]

while stack:
    v = stack.pop()

    if v not in visited:
        visited[v] = count
        count += 1

        tmp = []
        for g in graph[v]:
            heapq.heappush(tmp, -g)
        while tmp:
            stack.append(-heapq.heappop(tmp))



for i in range(1,vertex+1):
    print(visited[i])