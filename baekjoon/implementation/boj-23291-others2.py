# 어항 정리
from collections import deque

n, k = map(int, input().split())
bowl = []
bowl.append(deque(list(map(int, input().split()))))
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def put_one_fish_to_min(bowl):
    min_num = min(bowl[0])
    for i in range(len(bowl[0])):
        if bowl[0][i] == min_num:
            bowl[0][i] += 1

def popleft_upload(bowl):
    left_bowl = bowl[0].popleft()
    bowl.append(deque([left_bowl]))

def bowl_fly_and_rotate(bowl):
    while True:
        if len(bowl) > len(bowl[0]) - len(bowl[-1]):
            break
        fly_bowl = []
        for i in range(len(bowl)):
            tmp = deque()
            for _ in range(len(bowl[-1])):
                tmp.append(bowl[i].popleft())
            fly_bowl.append(tmp)
        bowl = [bowl[0]]
        tmp2 = [[0] * len(fly_bowl) for _ in range(len(fly_bowl[0]))]
        for i in range(len(fly_bowl[0])):
            for j in range(len(fly_bowl)):
                tmp2[i][j] = fly_bowl[j][len(fly_bowl[0]) -1 -i]
        rotated = tmp2
        for r in rotated:
            bowl.append(deque(r))
    return bowl

def change_fishnum(bowl):
    l = [[0] * len(bowl[x]) for x in range(len(bowl))]
    for x in range(len(bowl)):
        for y in range(len(bowl[x])):
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < len(bowl) and 0 <= ny < len(bowl[nx]):
                    if bowl[x][y] > bowl[nx][ny]:
                        d = (bowl[x][y] - bowl[nx][ny]) // 5
                        if d >= 1:
                            l[x][y] -= d
                    else:
                        d = (bowl[nx][ny] - bowl[x][y]) // 5
                        if d >= 1:
                            l[x][y] += d
    for i in range(len(bowl)):
        for j in range(len(bowl[i])):
            bowl[i][j] += l[i][j]

def change_bowl_toline(bowl):
    tmp = deque()
    for i in range(len(bowl[-1])):
        for j in range(len(bowl)):
            tmp.append(bowl[j][i])

    for i in range(len(bowl[-1]), len(bowl[0])):
        tmp.append(bowl[0][i])

    l = list()
    l.append(tmp)

    return l

def bowl_fly_and_rotate_center(bowl):
    a, b = list(), list()
    tmp = deque()
    for i in range(n//2):
        tmp.append(bowl[0].popleft())
    a.append(tmp)
    tmp2 = []
    for i in reversed(range(len(a))):
        a[i].reverse()
        tmp2.append(a[i])
    rotated1 = tmp2
    bowl += rotated1

    for i in range(2):
        tmp3 = deque()
        for j in range(n//4):
            tmp3.append(bowl[i].popleft())
        b.append(tmp3)
    tmp4 = []
    for i in reversed(range(len(b))):
        b[i].reverse()
        tmp4.append(b[i])
    rotated2 = tmp4
    bowl += rotated2

def diff_maxmin(bowl):
    return (max(bowl[0]) - min(bowl[0]))

cnt = 0
while True:
    diff = diff_maxmin(bowl)
    if diff <= k:
        print(cnt)
        break
    put_one_fish_to_min(bowl)
    popleft_upload(bowl)
    bowl = bowl_fly_and_rotate(bowl)
    change_fishnum(bowl)
    bowl = change_bowl_toline(bowl)
    bowl_fly_and_rotate_center(bowl)
    change_fishnum(bowl)
    bowl = change_bowl_toline(bowl)
    cnt += 1
