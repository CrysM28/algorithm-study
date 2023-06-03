# 10476. 좁은 미술전시관

N, k = map(int, input().split())
gal = []
for _ in range(N):
    gal.append(list(map(int, input().split())))
input()

if k == 0:
    ans = 0
    for g in gal:
        ans += g[0] + g[1]
    print(ans)
else:
    # i: 행 번호, j: 현재까지 닫힌 개수, k: L, R, both 순서대로 열림
    dp = [[[0, 0, 0] for _ in range(k+1)] for _ in range(N)]

    L, R = gal[0][0], gal[0][1]
    dp[0][1][0] = L
    dp[0][1][1] = R
    dp[0][0][2] = L+R

    for i in range(1, N):
        L = gal[i][0]
        R = gal[i][1]

        for j in range(k+1):
            if j >= 1:
                dp[i][j][0] = max(dp[i-1][j-1][0], dp[i-1][j-1][2]) + L
                dp[i][j][1] = max(dp[i-1][j-1][1], dp[i-1][j-1][2]) + R
            if i+1 > j:
                dp[i][j][2] = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2]) + L + R
        
    print(*dp, sep='\n')
    print(max(dp[-1][-1]))








            # if j == 0:
            #     dp[i][0][2] = dp[i-1][0][2] + L + R
            # else:
            #     left = dp[i-1][j-1][0]
            #     right = dp[i-1][j-1][1]
            #     both = dp[i-1][j][2]

            #     # if left == right == both == 0:
            #     #     continue

            #     dp[i][j][0] = max(left, both) + L 
            #     dp[i][j][1] = max(right, both) + R
            #     dp[i][j][2] = max(dp[i-1][j][0], dp[i-1][j][1], both) + L + R


                # left = dp[i-1][j-1][0] + L
                # right = dp[i-1][j-1][1] + R

                # both_prev_left = dp[i-1][j][0] + L + R
                # both_prev_right = dp[i-1][j][1] + L + R

                # dp[i][j][0] = left
                # dp[i][j][1] = right

                # if both_prev_right > left:
                #     dp[i][j][0] = both_prev_right
                # if both_prev_left > right:
                #     dp[i][j][1] = both_prev_left
