# 인접 행렬 - 2차원 배열
vertex, edge = map(int, input().split())
adj = [[0] * (vertex + 1) for _ in range(vertex + 1)]

for i in range(edge):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1



# 인접 리스트 - dict
from collections import defaultdict

vertex, edge = map(int, input().split())
adj = defaultdict(list)

for i in range(edge):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
