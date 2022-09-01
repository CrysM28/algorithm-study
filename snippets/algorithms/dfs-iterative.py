from collections import defaultdict

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
# 스택 구현
visited = []
stack = [start_v]

while stack:
    v = stack.pop()
    if v not in visited:
        visited.append(v)

        # 작은 번호부터 탐색하려면 인접리스트도 반대로 추가
        tmp = adj[v]
        while tmp:
            stack.append(tmp.pop())

####################################################################

# 탐색 순서대로 출력
print(*visited)
