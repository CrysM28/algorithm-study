# 7596. 토마토
import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(H) for _ in range(N)]

di = [1, -1, 0, 0, N, -N]  # i = 세로, 높이 (N, H)
dj = [0, 0, 1, -1, 0, 0]  # j = 가로 (M)
day = 1  # 날짜
unripe = False  # 안 익은 게 있는지 (0)
tomato = deque()  # 다음에 검사할 토마토 위치 큐

# 토마토 큐 초기화
for i in range(N * H):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((day, i, j))
        if box[i][j] == 0:
            unripe = True

# 안 익은 게 없으면 0
if not unripe:
    tomato = []
    day = 2


# 안 익은 게 있으면 익혀보기
while tomato:
    t = tomato.popleft()
    cur_day, i, j = t[0], t[1], t[2]

    if cur_day == day:
        day += 1

    # 안 익은 토마토 익히기 (익은 날짜로 표시)
    if box[i][j] == cur_day:
        for k in range(6):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N * H and 0 <= nj < M and box[ni][nj] == 0:
                if (di[k] == 1 or di[k] == -1) and ni // N != i // N:
                    continue  # 앞 뒤 일때 같은 층 아니면 X
                box[ni][nj] = day
                tomato.append((day, ni, nj))

# 더 익힐 수 없는데 못 익힌 게 남았으면 -1
for i in range(N * H):
    for j in range(M):
        if box[i][j] == 0:
            day = 1
            break

print(day - 2)
