# 21736. 헌내기는 친구가 필요해
from collections import deque

N, M = map(int, input().split())

grid = []
for i in range(N):
    line = list(input())
    grid.append(line)

    for j in range(M):
        if line[j] == 'I':
            doyeon = [i, j]

# print(doyeon)
# print(grid)

ans = 0

# BFS 탐색
queue = deque([doyeon])
visited =[[False] * M for _ in range(N)]
visited[doyeon[0]][doyeon[1]] = True

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

while queue:
    i, j = queue.popleft()

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]

        if 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] == 'O':
                grid[ni][nj] = 'V'
                queue.append([ni, nj])
                visited[ni][nj] = True
            if grid[ni][nj] == 'P':
                grid[ni][nj] = 'V'
                queue.append([ni, nj])
                visited[ni][nj] = True        
                ans += 1

if ans == 0:
    print('TT')
else:
    print(ans)

