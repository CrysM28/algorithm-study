# 13016. 내 왼손에는 흑염룡이 잠들어 있다
# pypy3는 메모리초과, python3는 시간초과

from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


# 국가의 수 (정점)
N = int(input())

# 도로 정보 (간선)
graph = defaultdict(list)
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


# 트리의 지름 찾기와 같은 논리
def dfs(start_v):
    distance = [-1] * (N + 1)
    stack = [(start_v,0)]

    while stack:
        v, l = stack.pop()
        for node, cost in graph[v]:
            if distance[node] == -1:
                stack.append((node, l + cost))
        distance[v] = max(distance[v], l)
    return distance
            

# 현 정점에서 가장 거리가 먼 정점 구하기
for i in range(1, N+1):
    dist = dfs(i)
    print(dist)


# def dfs(v, l):
#     # 인접 노드 확인
#     for node, cost in graph[v]:
#         # 방문하지 않은 노드일 때
#         if distance[node] == -1:
#             # 현재까지의 거리 더하기
#             distance[node] = l + cost
#             # 재귀 -> DFS
#             dfs(node, l + cost)
# # 현 정점에서 가장 거리가 먼 정점 구하기
# for i in range(1, N+1):
#     distance = [-1] * (N + 1)
#     distance[i] = 0
#     dfs(i, 0)
#     print(max(distance))


