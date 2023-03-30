## 484 -> 248ms

from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque([(S, 0)])
visited = [-1] * (F+1)
visited[S] = 0

while queue:
    v, cnt = queue.popleft()

    if v == G:
        break

    # 이 부분이 깔끔하고 좋은듯
    for n in (v+U, v-D):
        if 0 < n <= F and visited[n] == -1:
            visited[n] = cnt+1
            queue.append((n, cnt+1))

if visited[G] > -1:
    print(visited[G])
else:
    print("use the stairs")