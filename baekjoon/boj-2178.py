# 2178. 미로 탐색
from collections import defaultdict, deque


# BFS: 큐 구현
def bfs():
    visited = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


# N X M 배열
N, M = map(int, input().split())
adj = []
for i in range(N):
    adj.append(list(map(int,input())))

print(adj)