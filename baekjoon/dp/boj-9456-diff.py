# 9456. 스티커
## i=2인 경우를 굳이 두지 말기
# 392 -> 332ms 로 살짝 줄어들긴 한다

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    # dp[i][j] = stickers[i][j]를 뗐을 때의 점수의 합 최대
    # i = 0, 1 / j = 0 ~ n
    dp = [[0] * n for _ in range(3)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for j in range(1, n):
        if j == 1:
            dp[0][1] = dp[1][j-1] + stickers[0][1]
            dp[1][1] = dp[0][j-1] + stickers[1][1]
            continue

        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + stickers[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + stickers[1][j]

    answer = max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])
    print(answer)