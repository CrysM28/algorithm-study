# 10870. 피보나치 수 5
# 브론즈2, 1초, 256MB, 0 <= n <= 20
# 재귀 -> PyPy3 128ms

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(int(input())))
