# 10830. 행렬 제곱
import sys
input = sys.stdin.readline

# 행렬 곱셈 (boj.kr/2740)
def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z


# 행렬 a의 b제곱 구하기 (분할정복)
def square(a, b):
    if b == 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= 1000
        return a
    
    tmp = square(a, b//2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = square(matrix, B)
for r in result:
    print(*r)
