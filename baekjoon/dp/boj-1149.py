# 1149. RGB 거리
## bottom-up DP 방식으로
from collections import defaultdict

n = int(input())    # home num
h = [list(map(int, input().split())) for _ in range(n)] # home

# 1부터 N까지 합의 최소값을 저장하는 dp table
dp = defaultdict(int)
dp[0] = [h[0][0], h[0][1], h[0][2]]

# 바로 전 값만 영향받는 rgb 최소값 저장
for i in range(1, n):
    i_r = min(h[i][0] + dp[i-1][1], h[i][0] + dp[i-1][2])
    i_g = min(h[i][1] + dp[i-1][0], h[i][1] + dp[i-1][2])
    i_b = min(h[i][2] + dp[i-1][0], h[i][2] + dp[i-1][1])
    dp[i] = [i_r, i_g, i_b]

print(min(dp[n-1]))