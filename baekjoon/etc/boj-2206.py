# 2206. 벽 부수고 이동하기
from collections import deque

EMPTY = 0
WALL = 1
VISITED = 2
VISITED_WALL = 3

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def bfs(target_i, target_j):
    # (i, j, 이동거리, 벽 부순 횟수)
    queue = deque([(0, 0, 1, 0)])
    grid[0][0] = VISITED

    while queue:
        #print(queue)
        i, j, move, wall_break = queue.popleft()

        # 목표지점 도달 시 종료
        if i == target_i and j == target_j:
            return move

        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]

            # 이동가능한 경우
            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == EMPTY:
                    queue.append((ni, nj, move + 1, wall_break))
                    # 벽 부순 경우와 아닌 경우
                    if wall_break == 0:
                        grid[ni][nj] = VISITED
                    else:
                        grid[ni][nj] = VISITED_WALL

                # 벽 부순 적 없으면 한 번 부수고 이동
                if grid[ni][nj] == WALL and wall_break == 0:
                    queue.append((ni, nj, move + 1, wall_break + 1))

                # 벽 부순 경로는 벽 안 부순 경우에는 지나갈 수 있게
                if grid[ni][nj] == VISITED_WALL and wall_break == 0:
                    queue.append((ni, nj, move + 1, wall_break))
                    grid[ni][nj] = VISITED

        #print(*grid, sep='\n')

    # 도달 못하면 -1
    return -1


# 시작 위치 (1, 1), 끝 위치 (n, m)
n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]

answer = bfs(n - 1, m - 1)
print(answer)
