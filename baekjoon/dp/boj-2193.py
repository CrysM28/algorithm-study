# 2193. 이친수

n = int(input())

# 0 개수, 1개수 따로 관리
dp_0 = [0] * n
dp_1 = [0] * n
dp_1[0] = 1

for i in range(1, n):
    dp_0[i] = dp_0[i-1] + dp_1[i-1]
    dp_1[i] = dp_0[i-1]

print(dp_0[n-1] + dp_1[n-1])
