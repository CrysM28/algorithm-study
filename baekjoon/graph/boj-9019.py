# 9019. DSLR
from collections import deque
import sys

input = sys.stdin.readline


# 연산
def DSLR(x):
    # D
    d = (x * 2) % 10000

    # S
    if x == 0:
        s = 9999
    else:
        s = x - 1

    sx = str(x)
    if len(sx) < 4:
        tmp = '0' * (4 - len(sx))
        sx = tmp + sx

    # L
    l = int(sx[1:] + sx[0])
    # R
    r = int(sx[-1] + sx[:-1])

    return (d, s, l, r)


# BFS로 하나씩 검사
def bfs(a, b):
    q = deque([a])

    while q:
        now = q.popleft()
        # b와 같으면 종료
        if now == b:
            return now

        # 연산 수행
        d, s, l, r = DSLR(now)

        # 연산 줄이기 -> 확인한 적 있으면 다시 확인 X
        if d not in checked:
            checked[d] = (now, 'D')
            q.append(d)
        if s not in checked:
            checked[s] = (now, 'S')
            q.append(s)
        if l not in checked:
            checked[l] = (now, 'L')
            q.append(l)
        if r not in checked:
            checked[r] = (now, 'R')
            q.append(r)


T = int(input())
for _ in range(T):
    # input
    A, B = map(int, input().split())

    # 계산
    checked = dict()  # 어디에서 왔는지 기록
    bfs(A, B)

    # 결과: 역추적
    answer = ''
    b = B
    while b != A:
        answer += checked[b][1]
        b = checked[b][0]
    print(answer[::-1]) # 역추적했으므로 거꾸로 출력