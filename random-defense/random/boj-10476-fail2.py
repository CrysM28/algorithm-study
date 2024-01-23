# 10476. 좁은 미술전시관
## 문제에 있는 제약으로는 이걸로만 해도 되는데...


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
    dp = [[[-1, -1] for _ in range(k+1)] for _ in range(N)]


    L = gal[0][0]
    R = gal[0][1]

    dp[0][0][0] = L+R
    dp[0][0][1] = L+R
    dp[0][1][0] = L
    dp[0][1][1] = R


    #print(*dp, sep='\n')

    for i in range(1, N):
        L = gal[i][0]
        R = gal[i][1]

        for j in range(k+1):
            if j == 0:
                dp[i][0][0] = dp[i-1][0][0] + L + R
                dp[i][0][1] = dp[i-1][0][0] + L + R
            else:
                if max(dp[i-1][j-1]) == -1:
                    continue

                both = max(dp[i-1][j]) + L + R
                left = dp[i-1][j-1][0] + L
                right = dp[i-1][j-1][1] + R
            
                dp[i][j][0] = left
                dp[i][j][1] = right

                if both > left:
                    dp[i][j][0] = both
                if both > right:
                    dp[i][j][1] = both


    print(*dp, sep='\n')

    print(max(dp[-1][-1]))