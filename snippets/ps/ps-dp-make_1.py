# 빼거나 나눠서 1 만드는 문제

import collections

# 입력 정수
x = int(input())

# 각 idx가 1이 되는 최소 연산 횟수 저장
dp = collections.defaultdict(int)

# 나누어떨어질 때 나눌 수
DIV1 = 2
DIV2 = 3
DIV3 = 5

# Bottom-up
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % DIV1 == 0:
        dp[i] = min(dp[i], dp[i // DIV1] + 1)
    if i % DIV2 == 0:
        dp[i] = min(dp[i], dp[i // DIV2] + 1)
    if i % DIV3 == 0:
        dp[i] = min(dp[i], dp[i // DIV3] + 1)

# 결과 출력
print(dp[x])
