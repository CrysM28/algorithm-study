# 13913. 숨바꼭질 4
from collections import deque


def hide_and_seek():
    queue = deque([N])
    next_q = []
    
    while queue:
        v = queue.popleft()

        if v == K:
            return visited

        # +1, -1, *2
        minus1 = v - 1
        plus1 = v + 1
        mult2 = v * 2

        if minus1 not in visited:
        # if visited[minus1] == 0:
            visited[minus1] = v
            next_q.append(minus1)
        if plus1 not in visited:
        # if visited[plus1] == 0:
            visited[plus1] = v
            next_q.append(plus1)
        if mult2 <= K*2 and mult2 not in visited:
        # if mult2 <= K and visited[mult2] == 0:
            visited[mult2] = v
            next_q.append(mult2)

        if minus1 == K or plus1 == K or mult2 == K:
            return visited

        if not queue:
            queue = deque(next_q)
            next_q.clear()


N, K = map(int, input().split())
visited = {N: -1}
# visited = [0 for _ in range(200001)]
# visited[N] = -1

# 뺄셈만 가능
if N >= K:
    time = N - K
    path = [i for i in range(N, K-1, -1)]
else:
    hide_and_seek()

    path = [K]
    next_path = K
    while True:
        prev = visited[next_path]
        if prev == -1:
            break
        next_path = prev
        path.append(prev)
    
    time = len(path) - 1
    path = path[::-1]


print(time)
print(*path)
