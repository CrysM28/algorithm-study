# 1904. 01타일
from collections import defaultdict
MOD = 15746

n = int(input())

dp = defaultdict(int)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n] % MOD)
