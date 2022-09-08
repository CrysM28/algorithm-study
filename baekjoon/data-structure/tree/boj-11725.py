# 11725. 트리의 부모 찾기
from collections import defaultdict, deque


n = int(input())
tree = defaultdict(list)
parent = [0 for _ in range(n+1)]

for i in range(n-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)


# BFS
visited = [1]
queue = deque([1])

while queue:
    v = queue.popleft()
    for w in tree[v]:
        if w not in visited:
            visited.append(w)
            queue.append(w)
            parent[w] = v


print(*parent[2:], sep="\n")