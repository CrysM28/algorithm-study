# 15683. 감시
import copy

EMPTY = 0
WALL = 6

EAST, WEST, SOUTH, NORTH = 0, 1, 2, 3

# 동서남북
di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

# cctv 종류별 방향 개수
rotate_num = [0, 4, 2, 4, 4, 1]


def look(dir, next_grid, i, j):
    ni, nj = i, j
    while 0 <= ni < N and 0 <= nj < M:
        if next_grid[ni][nj] == EMPTY:
            next_grid[ni][nj] = '#'
        elif next_grid[ni][nj] == WALL:
            break
        ni += di[dir]
        nj += dj[dir]


def check_cctv(num, rotate, next_grid, i, j):
    # 단방향
    if num == 1:
        look(rotate, next_grid, i, j)
    
    # 2방향 (반대)
    elif num == 2:
        if rotate == 0:
            look(EAST, next_grid, i, j)
            look(WEST, next_grid, i, j)
        else:
            look(SOUTH, next_grid, i, j)
            look(NORTH, next_grid, i, j)

    # 2방향 (직각)
    elif num == 3:
        if rotate == 0:
            look(NORTH, next_grid, i, j)
            look(EAST, next_grid, i, j)
        elif rotate == 1:
            look(EAST, next_grid, i, j)
            look(SOUTH, next_grid, i, j)
        elif rotate == 2:
            look(SOUTH, next_grid, i, j)
            look(WEST, next_grid, i, j)
        elif rotate == 3:
            look(WEST, next_grid, i, j)
            look(NORTH, next_grid, i, j)

    # 3방향
    elif num == 4:
        if rotate == 0:
            look(WEST, next_grid, i, j)
            look(NORTH, next_grid, i, j)
            look(EAST, next_grid, i, j)
        elif rotate == 1:
            look(NORTH, next_grid, i, j)
            look(EAST, next_grid, i, j)
            look(SOUTH, next_grid, i, j)
        elif rotate == 2:
            look(EAST, next_grid, i, j)
            look(SOUTH, next_grid, i, j)
            look(WEST, next_grid, i, j)
        elif rotate == 3:
            look(SOUTH, next_grid, i, j)
            look(WEST, next_grid, i, j)
            look(NORTH, next_grid, i, j)

    # 4방향
    elif num == 5:
        look(EAST, next_grid, i, j)
        look(WEST, next_grid, i, j)
        look(SOUTH, next_grid, i, j)
        look(NORTH, next_grid, i, j)


def dfs(depth, cur_grid):
    global blind

    if depth == len(cctv):
        #print(*cur_grid, sep='\n')

        cnt = 0
        for i in range(N):
            cnt += cur_grid[i].count(0)

        #print(blind, cnt)

        blind = min(blind, cnt)
        return
    

    i, j = cctv[depth]
    cur_cctv_num = cur_grid[i][j]
    rotate = rotate_num[cur_cctv_num]

    for r in range(rotate):
        next_grid = copy.deepcopy(cur_grid)
        check_cctv(cur_cctv_num, r, next_grid, i, j)
        dfs(depth+1, next_grid)



N, M = map(int, input().split())
blind = 0   # 사각지대
cctv = []   # cctv 좌표

grid = []
for i in range(N):
    data = list(map(int, input().split())) 
    grid.append(data)

    for j in range(M):
        if data[j] == EMPTY:
            blind += 1
        elif data[j] != WALL:
            cctv.append([i, j])
    

#print(*grid, sep='\n')
#print(blind)
#print(cctv)


dfs(0, copy.deepcopy(grid))
print(blind)