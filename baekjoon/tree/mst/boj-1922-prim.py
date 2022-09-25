# 1922. 네트워크 연결
## 프림으로 풀이 -> PyPy3: 820 ms
from collections import defaultdict
from heapq import heappop, heappush, heapify

def prim(graph, start_node):
    # 노드 방문여부 관리
    visited = defaultdict(list)
    visited[start_node] = 1 

    # 인접 간선
    adj = graph[start_node]
    heapify(adj)
    # 신장 트리 집합
    mst = []

    # 전체 가중치
    total_weight = 0

    while adj:
        # 가중치가 가장 적은 간선 추출
        weight, u, v = heappop(adj) 

        # 사이클 발생 방지 위해 방문하지 않은 노드만 처리
        if v not in visited:
            visited[v] = 1 
            mst.append((u,v)) # 신장 트리 집합에 추가
            total_weight += weight

            # 다음 인접 간선 탐색
            for edge in graph[v]: 
                if edge[2] not in visited:
                    heappush(adj, edge) # 우선순위 큐에 edge 삽입

    return total_weight



# 입력: 노드, 간선
V = int(input())
E = int(input())

# 그래프를 인접리스트로 저장
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, u, v))
    graph[v].append((w, v, u))     # 무향 그래프일시

print(prim(graph,1))
