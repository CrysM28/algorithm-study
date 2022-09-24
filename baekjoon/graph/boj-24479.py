# 24479. 알고리즘 수업 - 깊이 우선 탐색 1

from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

def dfs(v, visited=None):
    # 함수 재사용을 위해 기본값 인자에 mutable 주지 않기
    if visited is None:
        visited = []
    
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited

vertex, edge, start_v = map(int, input().split())

# 인접 리스트
graph = defaultdict(list)
for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for a in graph:
    graph[a].sort()

result = dfs(start_v)

if len(result) < vertex:
    for _ in range(vertex-len(result)):
        result.append(0)

for r in result:
    print(r)