# 금광
for _ in range(int(input())):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    # 2차원 dp 테이블 (금광 값으로 초기화)
    dp = []
    i = 0
    for _ in range(n):
        dp.append(gold[i:i+m])
        i += m
    
    # dp[0][j] = gold[0][j]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            left = dp[i][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    # 결과는 마지막 열의 최대값
    result = []
    for i in range(n):
        result.append(dp[i][m-1])
    print(max(result))