## 788ms

import sys
input = sys.stdin.readline

n = int(input())
t = []; p = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti); p.append(pi)

for i in range(n):
    if t[i] <= n-i:
        dp[i+t[i]] = max(dp[i+t[i]], dp[i]+p[i])
    dp[i+1] = max(dp[i+1], dp[i])
    print(dp)

print(max(dp))