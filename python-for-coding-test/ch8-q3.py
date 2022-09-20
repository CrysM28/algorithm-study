# 개미 전사
from collections import defaultdict

n = int(input())
food = list(map(int, input().split()))

# 각 idx까지 털었을 때 최대값
dp = defaultdict(int)

dp[0] = food[0]
dp[1] = max(food[0], food[1])

for i in range(2, n):
    dp[i] = max(dp[i - 2] + food[i], dp[i - 1])

print(dp[n - 1])
