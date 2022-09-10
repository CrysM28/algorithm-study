# 2407. 조합
from math import factorial
n, m = map(int, input().split())

ans = factorial(n) // (factorial(n-m) * factorial(m))

print(ans)


## others

# a = 1
# for i in range(0, m):
#     a = a * (n-i)
# for i in range(1, m+1):
#     a = a // i