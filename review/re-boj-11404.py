# 11404. 플로이드
## 최단거리 - 플로이드
INF = int(1e10)

n = int(input())
m = int(input())

# 최단거리 배열 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# Floyd
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과
for i in range(1, n+1):
    for g in graph[i][1:]:
        if g >= INF:
            print(0, end=" ")
        else: print(g, end=" ")
    print()