# 1562. 계단 수
MOD = int(1e9)
n = int(input())

# dp[길이][마지막수][방문비트] (length, last, bit)
dp = [[[0]*(1<<10) for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i][1<<i] = 1

# bottom-up DP
for i in range(2, n+1):
    for j in range(10):
        for k in range(1<<10):
            if j == 0:
                dp[i][j][(1<<j)|k] += dp[i-1][1][k]
            elif j == 9:
                dp[i][j][(1<<j)|k] += dp[i-1][8][k]
            else:
                dp[i][j][(1<<j)|k] += dp[i-1][j-1][k] + dp[i-1][j+1][k]

            dp[i][j][(1<<j)|k] %= MOD

ans = 0
for i in range(10):
    ans += dp[n][i][(1<<10)-1]
    ans %= MOD
print(ans)


