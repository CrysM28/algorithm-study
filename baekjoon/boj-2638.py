# 2638. 치즈
from collections import deque
import copy

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

VISITED = -1

def bfs(cur_grid):
    changed = False
    q = deque([[0, 0]])
    cur_grid[0][0] = VISITED

    while q:
        i, j = q.popleft()

        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]

            if 0 <= ni < N and 0 <= nj < M:
                if cur_grid[ni][nj] == 0:
                    q.append([ni, nj])
                    cur_grid[ni][nj] = VISITED
                elif cur_grid[ni][nj] > 0:
                    cur_grid[ni][nj] += 1
                
                if cur_grid[ni][nj] > 2:
                    grid[ni][nj] = 0
                    changed = True

    return changed


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

change = True
day = -1
while change:
    change = bfs(copy.deepcopy(grid))
    day += 1

print(day)