# 미래 도시
## 플로이드 워셜
import sys

INF = sys.maxsize

# 회사 수, 경로 수
n, m = map(int, input().split())

# 인접행렬 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1  # 양방향

# 경로: 1 -> k -> x
x, k = map(int, input().split())


# 플로이드 워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 결과 출력
ans = graph[1][k] + graph[k][x]

if ans >= INF:
    print(-1)
else:
    print(ans)