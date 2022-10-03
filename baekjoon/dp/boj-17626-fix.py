# 17626. Four Squares
## 다른 사람 풀이해서 시간 줄여보기
## 472ms ->

from collections import defaultdict

n = int(input())
dp = defaultdict(int)

# 완전제곱수 먼저 처리
for i in range(1, int(n**.5) + 1):
    dp[i**2] = 1
if dp[n] == 1:
    print(dp[n])

# 완전제곱수 아닐 때
else:
    for i in range(2, n + 1):
        if dp[i] == 1:
            continue

        # dp[제곱수] + dp[전체-제곱수] 끼리만 비교해도 최소 알 수 있음
        # dp[제곱수]는 항상 1
        dp[i] = 4
        for k in range(1, int(i**.5) + 1):
            dp[i] = min(dp[i], dp[i - k**2] + 1)
            # 최소 개수 찾았으면 바로 끝내기 가능
            if dp[i] == 2:
                break

    print(dp[n])