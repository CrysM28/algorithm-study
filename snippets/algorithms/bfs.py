from collections import defaultdict, deque

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
# 큐 구현
visited = [start_v]
queue = deque([start_v])

while queue:
    v = queue.popleft()
    for w in adj[v]:
        if w not in visited:
            visited.append(w)
            queue.append(w)

####################################################################

# 탐색 순서대로 출력
print(*visited)
