# 2748. 피보나치 수 3
# 골드2, 1초, 128MB, n <= 1e18
# DP -> 메모리 초과 
# 분할정복을 이용한 거듭제곱 -> PyPy3 ms


def multiply(x, y):
    if y == 1:
        return x % c

    m = multiply(x, y >> 1)  # //2

    if y % 2 == 0:
        return m * m % c
    else:
        return m * m * x % c

a, b, c = map(int, input().split())
result = multiply(a, b)
print(result)


from collections import defaultdict  

n = int(input())
fib = defaultdict(int)

fib[0] = 0
fib[1] = 1

# bottom-up
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n]%int(1e6))