# 단순히 규칙 찾으면 이렇긴 함

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])