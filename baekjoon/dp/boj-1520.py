# 1520. 내리막 길

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

def dfs(i, j):
    # 도착점 도달
    if i == M-1 and j == N-1:
        return 1

    # DP memoization
    if dp[i][j] != -1:
        return dp[i][j]

    # 방문 표시
    dp[i][j] = 0

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        
        if 0 <= ni < M and 0 <= nj < N and grid[i][j] > grid[ni][nj]:
            dp[i][j] += dfs(ni, nj)

    # print("--", i, j)
    # print(*dp, sep='\n')

    return dp[i][j]


M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

ans = dfs(0, 0)
print(ans)

