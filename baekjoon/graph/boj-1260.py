# 1260. DFS와 BFS
## DFS -> 스택/재귀 구현
## BFS -> 큐 구현

from collections import deque

n, m, v = map(int, input().split())

# 인접행렬
adj = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1

# DFS : 스택 구현
visited_dfs = []
stack = [v]

while stack:
    c = stack.pop()
    if c not in visited_dfs:
        visited_dfs.append(c)

        # 작은 번호부터 탐색하기 위해 reverse
        for i, w in list(enumerate(adj[c]))[::-1]:
            if w == 1:
                stack.append(i)
print(*visited_dfs)

# BFS : 큐 구현
visited_bfs = [v]
queue = deque([v])

while queue:
    c = queue.popleft()
    for i, w in enumerate(adj[c]):
        if w == 1 and i not in visited_bfs:
            visited_bfs.append(i)
            queue.append(i)

print(*visited_bfs)