# 11047. 동전 0
## 배수이므로 그리디로 풀 수 있는 문제

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = coins[::-1]
cnt = 0

for c in coins:
    if k == 0: break
    elif k < c: continue

    while k - c >= 0:
        k -= c
        cnt += 1
    
    # better solution: (300ms -> 108ms)
    ## cnt += k//c
    ## k %= c

print(cnt)