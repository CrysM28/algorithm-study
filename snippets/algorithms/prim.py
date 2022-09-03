from collections import defaultdict
from heapq import heappop, heappush, heapify


def prim(graph, start_node):
    # 노드 방문여부 관리
    visited = defaultdict(list)
    visited[start_node] = 1

    # 인접 간선
    adj = graph[start_node]
    heapify(adj)

    # 전체 가중치
    total_weight = 0

    while adj:
        # 가중치가 가장 적은 간선 추출
        weight, u, v = heappop(adj)

        # 사이클 발생 방지 위해 방문하지 않은 노드만 처리
        if v not in visited:
            visited[v] = 1  # 방문 표시
            total_weight += weight

            # 다음 인접 간선 탐색
            for edge in graph[v]:
                if edge[2] not in visited:  # 사이클 방지
                    heappush(adj, edge)

    return total_weight


# 입력: 정점, 간선, 시작 노드
V, E, start = map(int, input().split())

# 그래프를 인접리스트로 저장
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, u, v))
    graph[v].append((w, v, u))  # 무향 그래프일시

print(prim(graph, start))
