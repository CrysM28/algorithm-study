# 7576. 토마토
## 3D

from collections import deque

# 토마토 익히기
def ripe(st):
    day = 0
    change = False
    q = deque(st)
    next_q = []

    while q:
        i, j = q.popleft()
        height = i // N

        for x in range(6):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < N*H and 0 <= nj < M and box[ni][nj] == 0:
                if x < 3 and ni//N != height:
                    continue
                change = True
                box[ni][nj] = 1
                next_q.append((ni, nj))

        if not q:
            if not change:
                return day
            #print("===")
            #print(*box, sep='\n')

            day += 1
            change = False
            q = deque(next_q)
            next_q.clear()

    return day

# 안 익은 거 있는지 확인
def check_unripe(d):
    for i in range(N*H):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    return d


M, N, H = map(int, input().split())

di = (-1, 1, 0, 0, -N, N)
dj = (0, 0, -1, 1, 0, 0)

box = []
start_tomato = []

for i in range(N*H):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 1:
            start_tomato.append((i, j))
    box.append(data)


#print(*box, sep='\n')
#print(start_tomato)

day = ripe(start_tomato)
day = check_unripe(day)
print(day)

