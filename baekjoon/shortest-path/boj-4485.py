# 4485. 녹색 옷 입은 애가 젤다지?

from heapq import heappush, heappop

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

def bfs():
    visited = [[0]*n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]

    while heap:
        #print(heap)
        val, i, j = heappop(heap)
        #print(val, i, j)

        if i == j == n-1:
            return val
      
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]

            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                heappush(heap, (val+grid[ni][nj], ni, nj))

    return 0


i = 1
while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]

    ans = bfs()
    print("Problem {}: {}".format(i, ans))
    i += 1