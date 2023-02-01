# 2740. 행렬 곱셈

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

res = [[0]*K for _ in range(N)]

for row in range(N):
    for col in range(K):
        val = 0
        for i in range(M):
            val += A[row][i] * B[i][col]
        res[row][col] = val

for r in res:
    print(*r)