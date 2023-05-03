# 14940. 쉬운 최단거리
from collections import deque

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

n,m = map(int, input().split())
grid = []
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    grid.append(data)

    for j in range(m):
        if data[j] == 2:
            start_i = i
            start_j = j
        if data[j] == 0:
            visited[i][j] = 0

# bfs
visited[start_i][start_j] = 0
queue = deque([(0, start_i, start_j)])

while queue:
    dist, i, j = queue.popleft()

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m:
            if visited[ni][nj] == -1 and grid[ni][nj] != 0:
                visited[ni][nj] = dist + 1
                queue.append((dist+1, ni, nj))

for v in visited:
    print(*v)