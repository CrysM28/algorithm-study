# 3197. 백조의 호수

WATER = '.'
ICE = 'X'
SWAN = 'L'
SWAN1 = '1'
SWAN2 = '2'

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

# pure water
def ice_to_water(cur_waters):
    next_waters = []

    for idx in range(len(cur_waters)):
        i, j = cur_waters[idx]

        if lake[i][j] != WATER:
            continue

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < R and 0 <= nj < C:
                if lake[ni][nj] == ICE:
                    lake[ni][nj] = WATER
                    next_waters.append([ni, nj])
                # elif lake[ni][nj] == SWAN1:
                #     lake[i][j] = SWAN1
                # elif lake[ni][nj] == SWAN2:
                #     lake[i][j] = SWAN2

    return next_waters


# swan group
def find_swan_group(queue, CUR_SWAN, OTHER_SWAN):
    next_queue = []
    visited = set()

    while queue:
        i, j = queue.pop()
        lake[i][j] = CUR_SWAN

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < R and 0 <= nj < C:
                if lake[ni][nj] == WATER:
                    lake[ni][nj] = CUR_SWAN
                    queue.append((ni, nj))
                elif lake[ni][nj] == ICE:
                    if (ni, nj) not in visited:
                        lake[ni][nj] = CUR_SWAN
                        next_queue.append((ni, nj))
                        visited.add((ni, nj))
                elif lake[ni][nj] == OTHER_SWAN:
                    return True, []

    return False, next_queue


# R: row(i), C: column(j)
R, C = map(int, input().split())

# get lake info
lake = []
swan1_x, swan1_y = 2000, 2000
swan2_x, swan2_y = 2000, 2000
waters = []
for r in range(R):
    data = input()
    lake.append(list(data))
    
    is_swan = list(filter(lambda e:data[e] == SWAN, range(len(data))))
    if len(is_swan) == 2:
        swan1_x, swan1_y  = r, is_swan[0]
        swan2_x, swan2_y = r, is_swan[1]
    elif len(is_swan) == 1:
        if swan1_x == 2000:
            swan1_x, swan1_y  = r, is_swan[0]
        else:
            swan2_x, swan2_y = r, is_swan[0]

    is_water = list(filter(lambda e:data[e] == WATER, range(len(data))))
    for w in is_water:
        waters.append([r, w])

# print("swans")
# print(swan1_x, swan1_y, swan2_x, swan2_y)
# print(waters)

next1 = [[swan1_x, swan1_y]]
next2 = [[swan2_x, swan2_y]]
day = 0
is_meet = False

while not is_meet:
    # swan1
    is_meet, next1 = find_swan_group(next1, SWAN1, SWAN2)
    if is_meet:
        break

    day += 1

    # swan2
    is_meet, next2 = find_swan_group(next2, SWAN2, SWAN1)
    if is_meet:
        break

    # pure water melting ice
    if waters:
        waters = ice_to_water(waters)


    # print("== today lake", day)
    # print(*lake, sep='\n')
    # print(next1)
    # print(next2)
    # print("===============")


# print("== end", day)
# print(*lake, sep='\n')

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

===============
정답은 맞는데 시간초과가 나서 분리 집합을 활용해보려고 합니다 -> how?

disjoint set -> L을 기준으로 서로소 집합을 구성,
자기 주변으로 매 턴마다 하나씩 더해나가는 걸로 얼음 녹이기 구현하고

서로소 집합이 아니게 되는 순간?
즉 두개의 swan의 parent가 같아지는 순간이 둘이 만나는 순간이 될 것

2차원 배열의 disjoint set은 어떻게 구현하면 좋을까요...

===============
1. 가장 먼저 각 swan1, swan2를 기준으로 그룹 만들기
    -> SWAN을 기준으로 WATER만 union, ICE 만나면 끝내기
    -> BFS로 좌표 넣으면서 WATER면 union 실행하는 식으로? 만난 곳은 만난 거 표시하고
        전에 만든 visit 함수 쓰면 될듯

2. 얼음 녹이기 -> 기존의 BFS 활용
    -> 이건 전에 구현한 거 그대로 쓰면 될듯
    녹임과 동시에 그룹 만들기 -> 녹인 얼음에 맞닿은 물로 UNION


4. 루프 처음에 swan1, swan2 find 실행해서 같으면 멈추기
    그러고 루프 맨 마지막에는 day +1 넣으면 될듯?


==========
근데 이렇게 하면 기존 구현과 무슨 차이가?

ice_to_water를 지금처럼 O(n^2)으로 매번 ice 찾는 식으로 하면 안되고...
그룹을 기껏 만들었으니까 이걸 활용해야 할 거 같은데요

하나의 루프 (한 날)에
swan 기준으로 인접한 water면 
swan 기준 union하고 
bfs 큐에 넣고


인접한 게 ice면 bfs 말고 ice 큐에 따로 
ICE큐에 따로 넣고 더 넣지 말기?
BFS처럼...

===========
구현 방법
swan1, swan2 위치 찾은 상태에서

1. swan1부터 시작 -> 값 L1이라고 하자
2. 인접 공간 탐색
    1) if WATER
        L1으로 변경
        현 위치 bfs q에 삽입
    2) if ICE
        L1으로 변경
        현 위치 next q에 삽입
    3) if L2
        break -> 이 때가 움직일 수 있는 타이밍

3. swan2도 2와 동일하게 구현

4. 1~3 루프
    루프 마지막에 day +1 붙여두기




'''