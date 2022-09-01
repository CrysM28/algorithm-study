# 1389. 케빈 베이컨의 6단계 법칙
INF = int(1e9)  # 가중치: 무한

n, m = map(int, input().split())  # n: 노드, m: 간선
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 최단거리 배열 (2차원)

# 자기 자신 비용 = 0 으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보 입력 (무향그래프, 모든 가중치 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이컨 수 계산
kb = INF
who = 0
for a in range(1, n + 1):
    a_kb = 0
    for b in range(1, n + 1):
        a_kb += graph[a][b]
    if a_kb < kb:
        kb = a_kb
        who = a

print(who)
#print(*graph, sep="\n")