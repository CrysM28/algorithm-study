# 13023. ABCDE
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def dfs(v, depth, visited):
    global friends

    if depth == 5:
        friends = True
        return
    
    for w in graph[v]:
        if w not in visited:
            visited.append(w)
            dfs(w, depth+1, visited)
            visited.pop()


N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friends = False

for i in range(N):
    dfs(i, 1, [i])
    if friends:
        print("1")
        break

if not friends:
    print("0")
