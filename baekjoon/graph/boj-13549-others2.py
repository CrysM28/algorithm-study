# 13549. 숨바꼭질 3
## 0-1 BFS 활용하기

from collections import deque

MAX = 100001

N, K = map(int, input().split())

time = 0
visited = [False] * MAX
visited[N] = True

queue = deque([N])
next_q = []

while queue:
    x = queue.popleft()

    if x == K:
        print(time)
        break

    # *2는 현재 같이 처리
    if x*2 < MAX and not visited[x*2]:
        queue.appendleft(x*2)
        visited[x*2] = True

    for next in (x-1, x+1):
        if 0 <= next < MAX and not visited[next]:
            next_q.append(next)
            visited[next] = True

    if not queue:
        time += 1
        queue = deque(next_q)
        next_q.clear()

