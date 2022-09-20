# 효율적인 화폐 구성

INF = int(1e9)

# 종류, 가치의 합
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
# 가장 작은 화폐단위부터 확인해야 함
coins.sort()   

dp = [INF] * (m + 1)
dp[0] = 0

# Bottom-up
for c in coins:
    for i in range(c, m + 1):
        # (i - c)원을 만드는 방법이 존재하는 경우
        if dp[i-c] != INF:
            dp[i] = min(dp[i], dp[i-c] + 1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])


