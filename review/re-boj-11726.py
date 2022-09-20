# 11726. 2xn 타일링
## DP

import collections

n = int(input())
DIV = 10007

dp = collections.defaultdict(int)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])