# 1로 만들기

import collections

x = int(input())

# 각 idx가 1이 되는 최소 연산 횟수 저장
dp = collections.defaultdict(int)
dp[1] = 0

for i in range(2, x + 1):
    # 1 빼기
    dp[i] = dp[i - 1] + 1

    # 2 나누기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # 3 나누기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # 5 나누기
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)


print(dp[x])