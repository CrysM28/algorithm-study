# 화성 탐사
from collections import defaultdict
import heapq as h

INF = int(1e9)

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

def dijkstra():
    # 2차원 배열
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = mars[0][0]
    unvisited = [(mars[0][0], (0,0))]

    while unvisited:
        time, node = h.heappop(unvisited)
        i = node[0]
        j = node[1]

        if dist[i][j] < time:
            continue

        # 상하좌우
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]

            # 이동할 수 있으면
            if ni >= 0 and ni < n and \
                nj >= 0 and nj < n:

                # 경로 최소값 업데이트
                cost = time + mars[ni][nj]

                if dist[ni][nj] > cost:
                    dist[ni][nj] = cost
                    h.heappush(unvisited, (cost,(ni,nj)))

    return dist


for _ in range(int(input())):
    n = int(input())
    mars = [list(map(int, input().split())) for _ in range(n)]

    result = dijkstra()
    print(result[n-1][n-1])