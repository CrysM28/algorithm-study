# 9461. 파도반 수열

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())

    dp = defaultdict(int)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for i in range(6, n+1):
        dp[i] = dp[i-5] + dp[i-1]

    print(dp[n])