# 7576. 토마토
from collections import deque

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

# 토마토 익히기
def ripe(st):
    day = 0
    change = False
    q = deque(st)
    next_q = []

    while q:
        i, j = q.popleft()

        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
                change = True
                box[ni][nj] = 1
                next_q.append((ni, nj))

        if not q:
            if not change:
                return day
            day += 1
            change = False
            q = deque(next_q)
            next_q.clear()

    return day

# 안 익은 거 있는지 확인
def check_unripe(d):
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    return d


M, N = map(int, input().split())

box = []
start_tomato = []

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 1:
            start_tomato.append((i, j))
    box.append(data)


day = ripe(start_tomato)
day = check_unripe(day)
print(day)

