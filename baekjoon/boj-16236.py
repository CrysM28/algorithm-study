# 16236. 아기 상어

from collections import deque
import copy

EMPTY = 0
SHARK_INIT = 9
SHARK = 100
VISITED = -1
EDIBLE = -2

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

# 최단거리인 물고기 찾기
def bfs(cur_i, cur_j, cur_size):
    arr = copy.deepcopy(grid)
    fishes = []
    queue = deque([(0, cur_i, cur_j)])

    while queue:
        dist, i, j = queue.popleft()

        # 먹을 수 있는 물고기 있고 거리 멀면 더 볼 필요 없음
        if fishes and dist > fishes[0][0]:
            break

        # 상하좌우 탐색
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            # 이동할 수 있으면
            if 0 <= ni < n and 0 <= nj < n:
                # 빈 곳이거나 같은 크기면 그냥 이동
                if arr[ni][nj] == EMPTY or arr[ni][nj] == cur_size:
                    arr[ni][nj] = VISITED
                    queue.append((dist+1, ni, nj))
                # 먹을 수 있는 물고기면 잡아먹을 수 있는 리스트에 추가
                elif 0 < arr[ni][nj] < cur_size:
                    arr[ni][nj] = EDIBLE
                    fishes.append((dist+1, ni, nj))
    return fishes


n = int(input())
grid = []
for i in range(n):
    data = list(map(int, input().split()))
    grid.append(data)
    if SHARK_INIT in data:
        pos = (i, data.index(SHARK_INIT))

# 아기상어 정보
moves = 0
size = 2
cnt = size  # 다음 사이즈까지 남은 물고기


while True:
    # 최단거리 물고기 찾기
    result = bfs(pos[0], pos[1], size)
    # 먹을 수 있는 물고기가 더 없으면 끝
    if not result:
        break

    # dist, i, j 순 정렬
    result.sort()
    fish = result[0]

    # 물고기 먹기
    ## 움직이기
    moves += fish[0]
    grid[pos[0]][pos[1]] = EMPTY
    grid[fish[1]][fish[2]] = SHARK
    pos = (fish[1], fish[2])

    ## 먹기
    cnt -= 1
    if cnt == 0:
        size += 1
        cnt = size

    # print("====")
    # print(*grid, sep='\n')
    # print("====")



print(moves)