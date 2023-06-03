# 2225. 합분해

MOD = int(1e9)
N, K = map(int, input().split()) 
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0:
            dp[i][j] = 1
            continue
        if j == 0:
            continue
        elif j == 1:
            dp[i][j] = 1
            continue

        for k in range(i+1):
            dp[i][j] += dp[k][j-1] % MOD


#print(*dp, sep='\n')

print(dp[-1][-1] % MOD)

        
