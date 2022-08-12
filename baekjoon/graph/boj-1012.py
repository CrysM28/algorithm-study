# 1012. 유기농 배추

import sys
sys.setrecursionlimit(10**4)

def dfs(i, j):
    # 종료조건
    if i >= n or i < 0 or \
        j >= m or j < 0 or \
            grid[i][j] != 1:
            return 
    
    # 방문 표시
    grid[i][j] = 0

    # 상하좌우 dfs 방문
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1

    for nn in range(n):
        for mm in range(m):
            if grid[nn][mm] == 1:
                dfs(nn, mm)
                cnt += 1

    print(cnt)
    #print(*grid, sep = "\n")

