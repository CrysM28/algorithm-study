# 9205. 맥주 마시면서 걸어가기
from collections import deque


def get_dist(pos1, pos2):
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    return x+y


for _ in range(int(input())):
    # 맥주 편의점 수
    n = int(input())

    # 좌표
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))


    is_happy = False

    q = deque(stores + [festival])
    next_q = []
    prev_q = []
    cur = home

    while q:
        next = q.popleft()

        dist = get_dist(cur, next)

        if dist <= 1000:
            if next == festival:
                is_happy = True
                break
            cur = next
        else:
            next_q.append(next)
        
        if not q and next_q:
            if prev_q == next_q:
                break
            prev_q = next_q[:]
            q = deque(next_q)
            next_q.clear()


    if is_happy:
        print("happy")
    else:
        print("sad")
