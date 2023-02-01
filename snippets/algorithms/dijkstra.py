from collections import defaultdict
from heapq import heappush, heappop
import sys

INF = sys.maxsize


# 최단거리 배열을 list로 사용할 때
def dijkstra_list(start):
    # 최단거리 배열 (dist[node] = time)
    dist = [INF for _ in range(V + 1)]
    dist[start] = 0

    # 미방문 상태인 정점 관리하는 우선순위 큐
    unvisited = [(0, start)]  # (time, node)

    # 우선순위 큐 이용, 매번 최단경로 삽입
    while unvisited:
        # 방문 표시
        time, node = heappop(unvisited)

        # 현재 노드가 이미 처리된 적이 있으면 무시
        if dist[node] < time:
            continue

        # 경로 정보 업데이트
        for v, w in graph[node]:
            alt = time + w
            # 현재 알려진 경로보다 현 노드를 거쳐 도달하는게 더 짧으면 갱신
            if dist[v] > alt:
                dist[v] = alt
                heappush(unvisited, (alt, v))

    return dist


# 최단거리 배열을 defaultdict로 사용할 때
def dijkstra_dict(start):
    # 최단거리 배열 (dist[node] = time)
    dist = defaultdict(int)

    # 미방문 상태인 정점 관리하는 우선순위 큐
    unvisited = [(0, start)]  # (time, node)

    # 우선순위 큐 이용, 매번 최단경로 삽입
    while unvisited:
        # 방문 표시
        time, node = heappop(unvisited)

        # 현재 노드가 이미 처리된 적이 있으면 무시
        if node not in dist:
            # 경로 정보 업데이트
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heappush(unvisited, (alt, v))

    # 도달할 수 없는 노드면 무한대로 값 변경
    if len(dist) != V:
        for i in range(1, V + 1):
            if i not in dist:
                dist[i] = INF

    return dist


# 입력: 정점, 간선, 시작 노드
V, E, start = map(int, input().split())

# 그래프를 인접리스트로 저장
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))     # 무향 그래프일시

# 출력
# d1 = dijkstra_list(start)
# print(d1)

# d2 = dijkstra_dict(start)
# print(d2)
