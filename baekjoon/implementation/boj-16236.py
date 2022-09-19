# 16236. 아기 상어
from collections import deque

def bfaas():
    visited = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


# 상하좌우 순
dx = (-1, 1, 0, 0)  
dy = (0, 0, -1, 1)


def bfs(shark):
    # 복사본
    cur_grid = grid[:]
    cur_time = 0

    visited = [shark]
    queue = deque([shark])

    while queue:
        v = queue.popleft()

        # 4방향 확인
        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]

            next_pos = [x,y]

            if 0 <= x < N and 0 <= y < N and next_pos not in visited:
                visited.append(next_pos)
                queue.append(next_pos)

        cur_time += 1

        print(queue)

    print(visited)
    return visited


    # # 인접 방향 탐색
    # ## 상하좌우
    # dfs(i-1, j) # 상
    # dfs(i+1, j) # 하
    # dfs(i, j-1) # 좌
    # dfs(i, j+1) # 우


    # # 종료 조건: 범위를 벗어나거나 더 탐색할 수 없으면 끝
    # if i < 0 or i >= N or \
    #     j < 0 or j >= N or \
    #         grid[i][j] != 1:
    #         return

    # # 탐색 마친 곳은 값을 변경
    # grid[i][j] = 0








# 공간의 크기
N = int(input())    

# 공간의 상태
grid = []
for i in range(N):
    tmp = list(map(int, input().split()))
    grid.append(tmp)

    # 상어 위치
    if 9 in tmp:
        pos = [i, tmp.index(9)]
    

# 상어 크기
size = 2
# 걸린 시간
time = 0



bfs(pos)

print(grid)


