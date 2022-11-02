# 3197. 백조의 호수
## 시간 초과
import copy
from collections import deque

WATER = '.'
ICE = 'X'
SWAN = 'L'
VISITED = 'O'

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def ice_to_water():
    next_lake = copy.deepcopy(lake)

    for i in range(R):
        for j in range(C):
            if lake[i][j] == ICE:
                for x in range(4):
                    ni = i + di[x]
                    nj = j + dj[x]

                    if 0 <= ni < R and 0 <= nj < C and lake[ni][nj] == WATER:
                        next_lake[i][j] = WATER
                        break

    return next_lake


def meet_swan():
    tmp_lake = copy.deepcopy(lake)
    tmp_lake[swan_x][swan_y] = VISITED

    queue = deque([(swan_x, swan_y)])
    while queue:
        i, j = queue.popleft()

        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]

            if 0 <= ni < R and 0 <= nj < C:
                if tmp_lake[ni][nj] == WATER:
                    tmp_lake[ni][nj] = VISITED
                    queue.append((ni, nj))
                if tmp_lake[ni][nj] == SWAN :
                    return True

    # print("== check swan move == ")
    # print(*tmp_lake, sep='\n')
    return False


R, C = map(int, input().split())

swan_x = 2000
swan_y = 2000
lake_org = []
for r in range(R):
    data = list(input())
    lake_org.append(data)

    if SWAN in data and swan_x == 2000 and swan_y == 2000:
        swan_x = r
        swan_y = data.index(SWAN)


lake = lake_org[:]
day = 0
is_meet = False

while not is_meet:

    if day == 0 and meet_swan():
        break

    # print(*lake, sep='\n')

    lake = ice_to_water()

    # print("== after day == ")
    # print(*lake, sep='\n')

    is_meet = meet_swan()
    day += 1

print(day)





'''
구현

BFS 시뮬레이션 구현같네요

매일 
1. 물 인접 얼음 녹이기
    -> 얼음을 확인해서 주위 물이면 물로 변하기
    -> 날이 지날수록 얼음이 줄고 물이 많아질 거니까 얼음 기준으로 구현하는 게 좋을듯

2. L에서 L 찾는 (X면 못 지나가는) BFS 구현해서 찾을 수 있으면 그 때를 return
    -> 못 찾으면 day +1 하고 다시 1 반복


'''