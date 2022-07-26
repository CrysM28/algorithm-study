from collections import defaultdict, deque

##############################################################

# BFS: 큐 구현
def bfs():
    visited = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


# DFS: 스택 구현
def dfs_iterative():
    visited = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)

            # 작은 번호부터 탐색하려면 인접리스트도 반대로 추가
            tmp = graph[v]
            while tmp:
                stack.append(tmp.pop())

    return visited


# DFS: 재귀 구현
def dfs_recursive(v, visited=None):
    # 함수 재사용을 위해 기본값 인자에 mutable 주지 않기
    if visited is None:
        visited = []
    
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs_recursive(w, visited)
    return visited

##############################################################

# 입력
vertex, edge, start_v = map(int, input().split())

# 인접 리스트
graph = defaultdict(list)
for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for a in graph:
    graph[a].sort()

# 탐색
# search = bfs()
# search = dfs_iterative()
# search = dfs_recursive(start_v)

# 탐색 순서대로 출력
# print(*search)
