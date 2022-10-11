# 1026. 보물

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

min_sum = 0

for i in range(n):
    min_sum += A[i] * B[i]

print(min_sum)