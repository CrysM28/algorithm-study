# 2293. 동전 1
## 경우의 수 

coins = []
n, k = map(int, input().split())
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1


for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

    #print(dp)

print(dp[-1])