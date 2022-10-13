# 9456. 스티커

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    # dp[i][j] = stickers[i][j]를 뗐을 때의 점수의 합 최대
    # i = 0, 1, 2(이전 스티커 안 뗐을 경우) / j = 0 ~ n
    dp = [[0] * n for _ in range(3)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[2][0] = 0

    for j in range(1, n):
        dp[0][j] = max(dp[2][j - 1], dp[1][j - 1]) + stickers[0][j]
        dp[1][j] = max(dp[2][j - 1], dp[0][j - 1]) + stickers[1][j]
        dp[2][j] = max(dp[0][j - 1], dp[1][j - 1])

    answer = max(dp[0][n-1], dp[1][n-1], dp[2][n-1])
    print(answer)