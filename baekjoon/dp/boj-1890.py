# 1890. 점프

N = int(input())
grid = [] 
for _ in range(N):
    grid.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = grid[i][j]

        # 0 예외처리 조심!!
        if jump == 0:
            break

        for ni, nj in ([i+jump, j], [i, j+jump]):
            if 0 <= ni < N and 0 <= nj < N:
                dp[ni][nj] += dp[i][j]


#print(*dp, sep='\n')
print(dp[-1][-1])