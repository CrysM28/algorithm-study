# 2749. 피보나치 수 3
# 골드2, 1초, 128MB, n <= 1e18
# DP -> 메모리 초과
# 분할정복을 이용한 거듭제곱 -> PyPy3 108ms

MOD = int(1e6)


# 행렬 곱셈
def matrix_mult(arr1, arr2):
    result = [[0] * 2 for _ in range(2)]
    result[0][0] = (arr1[0][0] * arr2[0][0] % MOD +
                    arr1[0][1] * arr2[1][0] % MOD) % MOD
    result[1][0] = (arr1[0][0] * arr2[0][1] % MOD +
                    arr1[0][1] * arr2[1][1] % MOD) % MOD
    result[0][1] = (arr1[1][0] * arr2[0][0] % MOD +
                    arr1[1][1] * arr2[1][0] % MOD) % MOD
    result[1][1] = (arr1[1][0] * arr2[0][1] % MOD +
                    arr1[1][1] * arr2[1][1] % MOD) % MOD
    return result


# 피보나치 - 분할 정복
def fib(n):
    if n == 1:
        return [[1, 1], [1, 0]]

    tmp = fib(n // 2)

    if n % 2 == 0:
        return matrix_mult(tmp, tmp)
    else:
        return matrix_mult(matrix_mult(tmp, tmp), fib(1))


n = int(input())

result = fib(n)
print(result[0][1])
