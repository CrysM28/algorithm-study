# 1697. 숨바꼭질
from collections import deque

MAX = 100001

N, K = map(int, input().split())

queue = deque([[N, 0]])
visited = [False] * MAX
visited[N] = True

while queue:
    x, time = queue.popleft()

    if x == K:
        print(time)
        break

    for v in (x+1, x-1, x*2):
        if 0 <= v < MAX and not visited[v]:
            visited[v] = True
            queue.append([v, time+1])


