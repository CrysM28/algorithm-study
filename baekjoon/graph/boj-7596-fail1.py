# 7596. 토마토
## 시간 초과

import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(H) for _ in range(N)]

di = [1, -1, 0, 0, N, -N]  # 앞 뒤 위 아래
dj = [0, 0, 1, -1, 0, 0]  # 오른쪽 왼쪽
day = 0  # 날짜
unripe = True  # 안 익은 게 있는지 (0)
ripe = True  # 그 날에 익힌 게 있는지


# 안 익은 게 있으면 계속 반복
while ripe:
    unripe = False
    ripe = False
    day += 1

    for i in range(N * H):  # i = 세로, 높이 (N, H)
        for j in range(M):  # j = 가로 (M)

            # 안 익은 토마토 익히기 (익은 날짜로 표시)
            if box[i][j] == day:
                for k in range(6):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < N * H and 0 <= nj < M and box[ni][nj] == 0:
                        if (di[k] == 1 or di[k] == -1) and ni // N != i // N:     
                            continue    # 앞 뒤 일때 같은 층 아니면 X
                        box[ni][nj] = day + 1
                        ripe = True

            # 안 익은 토마토 있는지 확인
            elif box[i][j] == 0:
                unripe = True

    # print("====", day)
    # print(*box, sep="\n")


# 더 익힐 수 없는데 못 익힌 게 남았으면
if unripe:  
    day = 0

print(day - 1)
