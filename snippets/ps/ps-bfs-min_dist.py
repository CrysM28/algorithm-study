# 시작에서 끝 위치까지 경로가 있을 때 최소거리 구하기

from collections import deque

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

# 상수
CAN = 1         # 이동할 수 있는 위치
VISITED = 2     # 이미 방문한 곳

def bfs(i, j):
    queue = deque([(0, 0, 1)])

    while queue:
        v = queue.popleft()

        # 끝 위치에 도달하면 종료
        if v[0] == i and v[1] == j:
            return v[2]

        for x in range(4):
            ni = v[0] + di[x]
            nj = v[1] + dj[x]

            # 이동할 수 있으면
            # if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == EMPTY:
            if ni >= 0 and ni < n and \
                nj >= 0 and nj < m and \
                arr[ni][nj] == CAN:
                # 방문 표시
                arr[ni][nj] = VISITED
                queue.append((ni, nj, v[2] + 1))

# 시작 위치 (1, 1), 끝 위치 (n, m)
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
# arr = []
# for _ in range(n):
#     arr += list(map(int, input())),

# 좌표 표현은 (1,1)부터지만 배열 입력은 (0,0)부터 받았으므로 -1로 넘기기
answer = bfs(n - 1, m - 1)
print(answer)
