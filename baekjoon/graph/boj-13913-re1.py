# 13913. 숨바꼭질 4
from collections import deque

MAX = 100001
N, K = map(int, input().split())
visited = [-1] * MAX
visited[N] = -2
queue = deque([[N, 0]])

while queue:
    x, t = queue.popleft()

    if x == K:
        print(t)
        ans = []
        while x != -2:
            ans.append(x)
            x = visited[x]
        print(*ans[::-1])
        break

    for next in (x-1, x+1, x*2):
        if 0 <= next < MAX and visited[next] == -1:
            visited[next] = x
            queue.append([next, t+1])
