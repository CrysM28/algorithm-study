# 섬의 개수

# 재귀 깊이 늘리기
import sys
sys.setrecursionlimit(10**4)

# DFS 재귀함수
def dfs(i, j):
    # 종료 조건: 범위를 벗어나거나 땅이 아니면 끝
    if i < 0 or i >= height or \
        j < 0 or j >= width or \
            grid[i][j] != 1:
            return

    # 탐색 마친 곳은 값을 변경
    grid[i][j] = 0

    # 8방향으로 dfs 수행
    dfs(i-1, j-1)
    dfs(i-1, j)
    dfs(i-1, j+1)
    dfs(i, j-1)
    dfs(i, j+1)
    dfs(i+1, j-1)
    dfs(i+1, j)
    dfs(i+1, j+1)

while True:

    # 입력 처리
    width, height = map(int, input().split())   # 너비, 높이
    if width == 0 and height == 0:
        break
    grid = []   # 지도
    for _ in range(height):
        grid += list(map(int, input().split())),


    # 땅을 찾으면 dfs 수행해서 물인곳 찾기
    island = 0   # 섬의 개수
    for h in range(height):
        for w in range(width):
            if grid[h][w] == 1:
                dfs(h, w)
                island += 1     # dfs 수행 한 번 마치고 나면 하나의 섬을 찾은 것

    print(island)


