# 15486. 퇴사 2
## 1016ms
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dp = defaultdict(int)

for i in range(N):
    time, price = map(int, input().split())
    dp[i + 1] = max(dp[i], dp[i+1])
    if time + i <= N:
        dp[i + time] = max(dp[i + time], dp[i] + price)

print(dp[N])
