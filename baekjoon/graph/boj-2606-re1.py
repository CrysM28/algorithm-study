# 2606. 바이러스
from collections import defaultdict, deque

def bfs():
    cnt = 0
    visited = set([1])
    queue = deque([1])

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if w not in visited:
                cnt += 1
                visited.add(w)
                queue.append(w)

    return cnt


N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs())