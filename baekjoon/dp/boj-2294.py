# 2294. 동전 2
## 가치가 다른 동전이 여러번 주어질 수 있다
## 사용한 최소 동전의 수

coins = []
n, k = map(int, input().split())
for _ in range(n):
    new_coin = int(input())
    if new_coin not in coins:
        coins.append(new_coin)

dp = [int(1e9)] * (k+1)
dp[0] = 0

#rint(coins)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

    #print(dp)

if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])