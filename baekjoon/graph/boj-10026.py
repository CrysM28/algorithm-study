# 10026. 적록색약

import copy
import sys
sys.setrecursionlimit(10**4)


# 적록색약이 아닌 사람
def rgb_search(i, j, color):
    # 종료 조건
    if i < 0 or i >= N or \
        j < 0 or j >= N or \
            grid[i][j] != color:
        return

    # 탐색 마친 곳은 값을 변경
    grid[i][j] = 'O'

    # 인접 방향 탐색
    rgb_search(i - 1, j, color)
    rgb_search(i + 1, j, color)
    rgb_search(i, j - 1, color)
    rgb_search(i, j + 1, color)


# 적록색약인 사람
def rg_search(i, j, color):
    # 범위 체크
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    
    # 색 체크 (R == G 취급)
    if grid[i][j] != color:
        if color != 'B' and (grid[i][j] == 'R' or grid[i][j] == 'G'):
            pass
        else:
            return

    grid[i][j] = 'O'

    rg_search(i - 1, j, color)
    rg_search(i + 1, j, color)
    rg_search(i, j - 1, color)
    rg_search(i, j + 1, color)



# 입력 받기
N = int(input())
grid_org = [list(input()) for _ in range(N)]

# 적록색약 아닌 사람
rgb_group = 0
grid = copy.deepcopy(grid_org)
for h in range(N):
    for w in range(N):
        if grid[h][w] != 'O':
            rgb_search(h, w, grid[h][w])
            rgb_group += 1
            # print("===")
            # print(*grid, sep='\n')

# 적록색약인 사람
rg_group = 0
grid = copy.deepcopy(grid_org)
for h in range(N):
    for w in range(N):
        if grid[h][w] != 'O':
            rg_search(h, w, grid[h][w])
            rg_group += 1
            # print("===")
            # print(*grid, sep='\n')


print(rgb_group, rg_group)
