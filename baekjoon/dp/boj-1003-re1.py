# 1003. 피보나치 함수

dp0 = [0] * 41
dp1 = [0] * 41

# 초기값
dp0[0], dp0[1] = 1, 0
dp1[0], dp1[1] = 0, 1

for i in range(2, 41):
    dp0[i] = dp0[i-1] + dp0[i-2]
    dp1[i] = dp1[i-1] + dp1[i-2]


for _ in range(int(input())):
    N = int(input())
    print(dp0[N], dp1[N])