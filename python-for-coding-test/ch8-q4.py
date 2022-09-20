# 바닥 공사
import collections
dp = collections.defaultdict(int)

n = int(input())

DIV = 796796
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % DIV

print(dp[n])
