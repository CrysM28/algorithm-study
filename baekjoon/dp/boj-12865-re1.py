# 12865. 평범한 배낭

N, K = map(int, input().split())
# (무게, 가치)
things = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

# i: 짐 개수, j: 최대 용량
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0:
            continue

        # 더 담을 수 있을 때
        elif things[i][0] <= j:
            # 비교: 지금 짐 + 지금 짐 무게 제외 이전 짐 vs 이전 짐
            dp[i][j] = max(things[i][1] + dp[i-1][j-things[i][0]], dp[i-1][j])
        
        # 더 담을 수 없을 때(용량초과) -> 이전 짐 그대로
        else:
            dp[i][j] = dp[i-1][j]


print(dp[-1][-1])