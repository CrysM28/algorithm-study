# 2579. 계단 오르기

n = int(input())  # 계단 개수
stair = [int(input()) for _ in range(n)]  # 계단 가중치
dp = []  # dp 테이블

# 초기값 (2 이하면 될때까지만 append)
try:
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
except IndexError:
    pass

# DP (bottom-up)
for i in range(3, n):
    dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]))

print(dp.pop())