# 2178. 미로 탐색

from collections import deque

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def bfs(i, j):
    queue = deque([(0, 0, 0)])

    while queue:
        v = queue.popleft()

        if v[0] == i and v[1] == j:
            return v[2]

        for x in range(4):
            ni = v[0] + di[x]
            nj = v[1] + dj[x]

            # 이동할 수 있으면
            if ni >= 0 and ni < n and \
                nj >= 0 and nj < m and \
                arr[ni][nj] == 1:
                # 방문 표시
                arr[ni][nj] = 2
                queue.append((ni, nj, v[2] + 1))


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr += list(map(int, input())),

answer = bfs(n - 1, m - 1)
print(answer + 1)
