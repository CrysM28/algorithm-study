from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

# 입력
vertex, edge, start_v = map(int, input().split())

# 인접 리스트
adj = defaultdict(list)
for i in range(edge):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
for a in adj:
    adj[a].sort()

####################################################################
# 재귀 구현
def dfs(v, visited=[]):
    visited.append(v)
    for w in adj[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited

ans = dfs(start_v)

####################################################################

# 탐색 순서대로 출력
print(*ans)
