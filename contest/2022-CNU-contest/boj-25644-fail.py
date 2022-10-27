# 25644. 최대 상승
## 시간 초과

N = int(input())
stocks_list = list(map(int, input().split()))

# 주가순 정렬
stocks = dict(enumerate(stocks_list))
stocks = sorted(stocks.items(), key = lambda item:item[1])
#print(stocks)

max_profit = 0
for sell in range(N-1, 0, -1):
    for buy in range(sell):
        if stocks[buy][0] <= stocks[sell][0]:
            cur_profit = stocks[sell][1] - stocks[buy][1]
            max_profit = max(cur_profit, max_profit)
            break

print(max_profit)


## DP
# from collections import defaultdict
# dp = defaultdict(int) 
# for i in range(1, N):
#     if stock[i] - stock[i-1] > 0:
#         dp[i] = dp[i-1] + stock[i] - stock[i-1]
#     else:
#         dp[i] = 0

# print(max(dp.values()))
