# 11728. 배열 합치기

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []
idx_A, idx_B = 0, 0 

while idx_A != N and idx_B != M:
    val_A, val_B = A[idx_A], B[idx_B]
    
    if val_A < val_B:
        arr.append(val_A)
        idx_A += 1
    else:
        arr.append(val_B)
        idx_B += 1

# 나머지 붙이기
if idx_A == N:
    arr += B[idx_B:]
else:
    arr += A[idx_A:]

print(*arr)