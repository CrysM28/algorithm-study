# 정확한 순위

INF = int(1e10)

n, m = map(int, input().split())

# 최단거리 배열 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# Floyd
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과
## [i][j] 나 [j][i] 중 둘 중 하나라도 도달 가능하면 순위를 매길 수 있음
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            break
    else:
        cnt += 1

print(cnt)
        