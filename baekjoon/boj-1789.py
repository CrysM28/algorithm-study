# 1789. 수들의 합

S = int(input())

n = 1
while n*(n+1)/2 <= S:
    n += 1

print(n-1)