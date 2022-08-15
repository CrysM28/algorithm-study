# 1463. 1로 만들기
## DP: top-down

import collections

n = int(input())
dp = collections.defaultdict(int)  # 연산횟수 저장

# bottom-up: dp 테이블 채워나가기
for i in range(2, n + 1):
    # /3, /2, -1 중 가장 작은 값으로 결정 (/는 나누어 떨어질때만)
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])