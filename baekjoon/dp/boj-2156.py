# 2156. 포도주 시식
## k번째를 안 마시는 경우도 고려!!

N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0] * N

try:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0] + wines[2], wines[1] + wines[2], dp[1])
except IndexError:
    pass


for i in range(3, N):
    dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i], dp[i-1])

print(max(dp))