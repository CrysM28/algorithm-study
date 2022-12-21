# 15486. 퇴사 2
## 1016ms
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
time = []
price = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)

dp = defaultdict(int)

for i in range(N-1, -1, -1):
    if time[i] + i <= N:
        dp[i] = max(price[i] + dp[i + time[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
