import collections

x = int(input())
dp = collections.defaultdict(int)

# Bottom-up으로 만들어가기
for i in range(2, x + 1):
    # 가능한 min 값 계산
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])
