# 25644. 최대 상승
N = int(input())
stock = list(map(int, input().split()))

min_val = int(1e10)
max_profit = 0

for s in stock:
    if min_val > s:
        min_val = s
    
    cur_profit = s - min_val
    max_profit = max(max_profit, cur_profit)

print(max_profit)
