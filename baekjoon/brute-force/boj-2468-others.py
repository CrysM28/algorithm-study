from collections import *

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
Ans = 1
Dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for k in range(1, 101):
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Map[i][j] > k and visit[i][j] == 0:
                D = deque()
                cnt += 1
                visit[i][j] = 1
                D.append((i, j))

                while D:
                    x, y = D.popleft()

                    for a, b in Dir:
                        nx = a + x
                        ny = b + y
                        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and Map[nx][
                                ny] > k and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            D.append((nx, ny))
    Ans = max(Ans, cnt)

print(Ans)