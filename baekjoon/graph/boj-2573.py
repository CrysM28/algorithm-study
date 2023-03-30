# 2573. 빙산
import copy
import sys

sys.setrecursionlimit(10**4)

di = (0,0,1,-1)
dj = (1,-1,0,0)

def dfs(i, j):
    if cur_grid[i][j] <= 0:
        return

    cur_grid[i][j] = -1

    for x in range(4):
        ni, nj = i+di[x], j+dj[x]

        if not(0<=ni<N) or not(0<=nj<M):
            continue

        if cur_grid[ni][nj] == 0:
            grid[i][j] -= 1
            if grid[i][j] < 0:
                grid[i][j] = 0
        else:
            dfs(i+di[x], j+dj[x])


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

#print(*grid, sep='\n')

year = 0

while True:
    cur_grid = copy.deepcopy(grid)
    ice = 0

    for i in range(N):
        for j in range(M):
            if cur_grid[i][j] > 0:
                dfs(i, j)
                ice += 1

    print("===")
    print(*cur_grid, sep='\n')
    print("--")
    print(*grid, sep='\n')
    print(ice)

    if ice >= 2:
        break
    elif ice == 0:
        year = 0
        break

    year += 1


print(year)