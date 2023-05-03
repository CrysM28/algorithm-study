# 2293. 동전 1

coins = []
n, k = map(int, input().split())
for _ in range(n):
    coins.append(int(input()))


dp = [set() for _ in range(k+1)]

for i in range(1, k+1):
    #print("==", i)
    for c in range(n):
        # 하나의 동전만
        q, r = divmod(i, coins[c])
        if r == 0:
            coin_set = [coins[c]] * q
            coin_set = tuple(coin_set)
            #print(coin_set)
            dp[i].add(coin_set)
        
        # 여러 동전 사용
        if i - coins[c] > 0:
            for d in dp[i-coins[c]]:
                coin_set = list(d) + [coins[c]]
                coin_set.sort()
                coin_set = tuple(coin_set)

                #if coin_set not in dp[i]:
                dp[i].add(coin_set)


print(len(dp[-1]))


print(*dp, sep='\n')
