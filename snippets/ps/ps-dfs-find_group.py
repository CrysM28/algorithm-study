# 주어진 배열/그래프에서 그룹 개수 찾기
# 자주 나오는 DFS 문제

## 가정
### 주어진 2차원 grid에서 인접한 1의 묶음이 몇 개인지 세는 문제
### 인접의 기준은 보통 상하좌우(+ 대각선)


# 재귀 깊이 늘리기
import sys
sys.setrecursionlimit(10**4)

# 상수
CAN = 1         # 이동할 수 있는 위치
VISITED = 2     # 이미 방문한 곳


# DFS 재귀함수
def dfs(i, j):
    # 종료 조건: 범위를 벗어나거나 더 탐색할 수 없으면 끝
    if i < 0 or i >= height or \
        j < 0 or j >= width or \
            grid[i][j] != CAN:
            return

    # 탐색 마친 곳은 값을 변경
    grid[i][j] = VISITED

    # 인접 방향 탐색
    ## 상하좌우
    dfs(i-1, j) # 상
    dfs(i+1, j) # 하
    dfs(i, j-1) # 좌
    dfs(i, j+1) # 우
    ## 대각선
    dfs(i-1, j-1)   # 좌상
    dfs(i-1, j+1)   # 좌하
    dfs(i+1, j-1)   # 우상
    dfs(i+1, j+1)   # 우하

# 입력 받기
height, width = map(int, input().split())   # N x M 일 때, height == N, width == M
grid = [list(input()) for _ in range(height)]

# 인접한 1의 그룹 개수
group = 0 

# 2차원 배열의 모든 원소를 한 번씩 확인
for h in range(height):
    for w in range(width):
        # 기준이 되는 1을 찾으면 dfs로 탐색 
        # 한 번 탐색된 곳은 값이 바뀌므로 다시 탐색되지 않음
        if grid[h][w] == CAN:
            dfs(h, w)
            # dfs 재귀가 한 번 끝나면 하나의 묶음을 찾은 것
            group += 1 

# 결과 출력
print(group)


