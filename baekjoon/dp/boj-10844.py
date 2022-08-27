# 10844. 쉬운 계단 수
from collections import defaultdict
dp = defaultdict(defaultdict)   # 2차원 동적배열

n = int(input())

# 기본값
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1

## bottom-up
for l in range(2,n+1):
    # 바로 1개 전 자릿수(길이, l)의 경우의 수에 현재 끝자리(i)만 붙이기
    for i in range(0,10):
        # 0보다 작은 숫자 없으므로 i+1, 즉 1만
        if i == 0:
            dp[l][0] = dp[l-1][1]
        # 9보다 큰 숫자 없으므로 i-1, 즉 8만
        elif i == 9:
            dp[l][9] = dp[l-1][8]
        # 계단수이므로 앞에 +-1 
        else:
            dp[l][i] = dp[l-1][i-1] + dp[l-1][i+1]

total = 0
for i in range(10):
    total += dp[n][i]

print(total%int(10e8))
