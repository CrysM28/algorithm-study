# 10826. 피보나치 수 4
# 실버5, 1초, 256MB, n <= 10000
# DP -> PyPy3 160ms
## 이 문제는 임의 정밀도/큰 수 연산 문제라 파이썬에서는 상관없는 부분인듯

from collections import defaultdict

n = int(input())
fib = defaultdict(int)

fib[0] = 0
fib[1] = 1

# bottom-up
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n])