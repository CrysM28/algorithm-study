# 2748. 피보나치 수 2
# 브론즈1, 1초, 256MB, n <= 90
# 재귀 -> 시간 초과
# DP -> PyPy3 148ms

from collections import defaultdict

n = int(input())
fib = defaultdict(int)

fib[0] = 0
fib[1] = 1

# bottom-up
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n])