# 이것도 172ms로 짧게 끝남

from sys import stdin

n = int(stdin.readline())
## 처음부터 최대값으로 초기화하는 것도 괜찮은듯
dp = [4 for _ in range(50001)]
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3


for cur in range(4, 50001):
    if int(cur ** (1/2)) == cur ** (1/2):
        dp[cur] = 1
        continue
    for i in range(1, int(cur ** (1/2)) + 1):
        dp[cur] = min(dp[cur], dp[cur - i**2] + 1)
print(dp[n])