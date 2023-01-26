# 11047. 동전 0

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0

for i in range(n-1, -1, -1):
    c = k // coins[i]
    cnt += c
    k -= coins[i] * c

print(cnt)