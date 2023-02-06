# 2098. 외판원 순회
import sys
input = sys.stdin.readline

def dfs(x, visited):
    # 모든 도시 방문 완료
    if visited == (1 << n) - 1:
        # 출발점으로 돌아갈 수 있음
        if graph[x][0] != 0:
            dp[x][visited] = graph[x][0]
            return graph[x][0]
        else:
            return INF
    
    # 이미 계산했으면 스킵
    if dp[x][visited] != -1:
        return dp[x][visited]

    min_dist = INF
    # 모든 도시 탐방
    for i in range(1, n):
        # 아직 방문하지 않았고 가는 경로가 있으면
        if visited & (1 << i) == 0 and graph[x][i] != 0:
            min_dist = min(min_dist, dfs(i, visited | (1 << i)) + graph[x][i])
    
    dp[x][visited] = min_dist
    return min_dist


INF = int(1e9)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n)]

print(dfs(0, 1))
