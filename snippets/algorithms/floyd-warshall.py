INF = int(10e9)

# 입력: 정점, 간선, 시작 노드
V, E, start = map(int, input().split())

# 최단거리 배열
graph = [[INF] * (V + 1) for _ in range(V + 1)]
for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    # graph[a][b] = min(graph[a][b], c) # 같은 간선, 다른 가중치가 들어올 때
    # graph[b][a] = c   # 무향 그래프일때

# 플로이드-워셜
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, V + 1):
    for b in range(1, V + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()