from collections import defaultdict, deque

# 전체 사람
n = int(input())
# 촌수 계산
a, b = map(int, input().split())
# 관계 개수
m = int(input())
# 관계
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = []
q = deque([a])
next_q = []
ans = 0
find_rel = False

while q:
    v = q.popleft()

    if v == b:
        find_rel = True
        break


    for w in graph[v]:
        if w not in visited:
            visited.append(w)
            next_q.append(w)
    
    if not q:
        q = deque(next_q)
        next_q.clear()
        ans += 1


if find_rel:
    print(ans)
else:
    print(-1)

