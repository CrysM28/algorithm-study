# 2096. 내려가기

INF = int(1e9)
max_dp = [[0]*3 for _ in range(2)]
min_dp = [[0]*3 for _ in range(2)]

N = int(input())

for _ in range(N):
    a,b,c = map(int, input().split())

    # max
    max_dp[0][0] = max_dp[1][0]
    max_dp[0][1] = max_dp[1][1]
    max_dp[0][2] = max_dp[1][2]

    max_dp[1][0] = max(max_dp[0][0]+a, max_dp[0][1] + a)
    max_dp[1][1] = max(max_dp[0][0]+b, max_dp[0][1]+b, max_dp[0][2]+b)
    max_dp[1][2] = max(max_dp[0][1]+c, max_dp[0][2]+c)

    # min
    min_dp[0][0] = min_dp[1][0]
    min_dp[0][1] = min_dp[1][1]
    min_dp[0][2] = min_dp[1][2]

    min_dp[1][0] = min(min_dp[0][0]+a, min_dp[0][1]+a)
    min_dp[1][1] = min(min_dp[0][0]+b, min_dp[0][1]+b, min_dp[0][2]+b)
    min_dp[1][2] = min(min_dp[0][1]+c, min_dp[0][2]+c)


max_val = max(max_dp[1])
min_val = min(min_dp[1])
print(max_val, min_val)