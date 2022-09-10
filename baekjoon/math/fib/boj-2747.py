# 2747. 피보나치 수
# 브론즈2, 1초, 256MB, n <= 45
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