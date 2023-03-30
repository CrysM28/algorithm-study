# 13460. 구슬 탈출 2
from collections import deque

di = (0, 0, -1, 1)
dj = (-1, 1, 0, 0)

def turn(d, i, j):
    cnt = 0
    while board[i+di[d]][j+dj[d]] != '#' and board[i][j] != 'O':
        i += di[d]
        j += dj[d]
        cnt += 1
    return i, j, cnt


def bfs():
    cnt = 1
    q = deque([(red_i, red_j, blue_i, blue_j)])
    next_q = []
    visited = {(red_i, red_j, blue_i, blue_j)}

    while q:
        ri, rj, bi, bj = q.popleft()

        # 횟수 초과
        if cnt > 10:
            break

        for dir in range(4):
            nri, nrj, rcnt = turn(dir, ri, rj)
            nbi, nbj, bcnt = turn(dir, bi, bj)

            # B가 들어가면 무조건 실패
            if board[nbi][nbj] != 'O':
                # 성공
                if board[nri][nrj] == 'O':
                    print(cnt)
                    return

                # R과 B가 겹치면 더 많이 이동한 것을 한 칸 뒤로
                if (nri, nrj) == (nbi, nbj):
                    if rcnt > bcnt:
                        nri -= di[dir]
                        nrj -= dj[dir]
                    else:
                        nbi -= di[dir]
                        nbj -= dj[dir]

                # 다음 탐색
                if (nri, nrj, nbi, nbj) not in visited:
                    visited.add((nri, nrj, nbi, nbj))
                    next_q.append((nri, nrj, nbi, nbj))

        if not q:
            q = deque(next_q)
            next_q.clear()
            cnt += 1

    # 실패
    print(-1)


N, M = map(int, input().split())
board = []
red_i, red_j = 0, 0
blue_i, blue_j = 0, 0

for i in range(N):
    data = list(input())
    board.append(data)
    if 'R' in data:
        red_i = i
        red_j = data.index('R')
    if 'B' in data:
        blue_i = i
        blue_j = data.index('B')

bfs()