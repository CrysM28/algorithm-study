# 1309. 동물원

MOD = 9901

N = int(input())

# dp[N번째우리][0에만, 1에만, 둘다X]
#dp = [[0] * 3 for _ in range(N)]
dp = [[0] * 3 for _ in range(2)]

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1


for i in range(1, N):
    i %= 2
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = sum(dp[i-1]) % MOD


#print(*dp, sep='\n')

print(sum(dp[(N+1)%2])%MOD)