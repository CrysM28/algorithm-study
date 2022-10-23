# 1987. 알파벳
# deque 말고 set을 전체에다가 사용해야 함
from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

queue = deque([(0, 0, arr[0][0])])
next_queue = []
while queue:
    #print(queue)
    i, j, visited = queue.popleft()

    # 상하좌우 탐색
    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] not in visited:
            queue.append((ni, nj, visited + arr[ni][nj]))

    if not queue:
        final_visited = visited

print(len(final_visited))