# 1932. 정수 삼각형

import sys

input = sys.stdin.readline

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(len(dp[i])):
        # 맨 왼쪽
        if j == 0:
            dp[i][j] += dp[i - 1][j]

        # 맨 오른쪽
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i - 1][j - 1]

        # 가운데
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n-1]))