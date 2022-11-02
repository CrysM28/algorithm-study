# 2146. 다리 만들기
## PyPy3 3828ms

from collections import deque
import copy

SEA = 0
LAND = 1
BRIDGE = 2
VISITED = 0
INF = int(1e9)
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

n = int(input())
country = [list(map(int, input().split())) for _ in range(n)]

min_bridge = INF


def find_min_bridge(start_i, start_j):
    # 임시 지도
    grid = copy.deepcopy(country)   
    island = deque([[start_i, start_j]])
    country[start_i][start_j] = VISITED
    grid[start_i][start_j] = VISITED
    q = deque([])
    next_q = []

    # 전처리: 전체 지도에 섬 방문 표시 & 외곽 좌표 q에 추가
    while island:
        i, j = island.popleft()
        
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == LAND:
                    grid[ni][nj] = VISITED
                    country[ni][nj] = VISITED
                    island.append([ni, nj])
                elif grid[ni][nj] == SEA:
                    grid[ni][nj] = BRIDGE
                    q.append([ni, nj])


    print("grid")
    print(*grid, sep='\n')

    # 최소 거리 찾기: 다른 섬 만날때까지 
    bridge_len = 1
    connected = False

    while q:
        i, j = q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < n and 0 <= nj < n:
                # 다른 섬 만나면 끝
                if (grid[ni][nj] < 0 and grid[ni][nj] != VISITED) or grid[ni][nj] == LAND:
                    connected = True
                    break
                # 계속 다리 잇기
                elif grid[ni][nj] == SEA:
                    grid[ni][nj] = BRIDGE
                    next_q.append([ni, nj])
                    
        # 연결 완료
        if connected:
            return bridge_len

        # 다음 길이
        if not q:
            q = deque(next_q)
            next_q.clear()
            bridge_len +=1

        # 전에 구한 최소값을 넘어가면 더 보지 않고 종료
        if bridge_len > min_bridge:
            return INF

    return bridge_len


for i in range(n):
    for j in range(n):
        if country[i][j] == LAND:
            VISITED -= 1
            cur_min = find_min_bridge(i, j)
            min_bridge = min(min_bridge, cur_min)

print(min_bridge)









'''
섬 구분은 DFS find-group 응용
섬 간의 최소거리니까 BFS

1. 섬 구분: DFS find-group 응용
일단 모든 grid 훑기

2. 최소거리 구하기 BFS
    1. 일단 전처리: 그 섬 육지는 모두 VISITED로 먼저 처리
        인접공간 상하좌우 검사
            LAND면 VISITED
            SEA면 BRIDGE 놓고 next_q에 추가
    2. 그 다음부터는 next_q가 빌때까지 1과 조금 다르게 처리
        루프 끝날때마다 bridge_len += 1
        >> LAND면 끝 -> 이때가 최소거리
        SEA면 BRIDGE 놓고 next_q에 추가 

3. 다음 섬에서 2 반복
    단, 현재 구한 bridge_len보다 길어지면 바로 종료 (어차피 그럼 최소거리 아니니까)


종료조건을 다른 섬을 만나는 걸로 하고 싶은데
현재 섬은 VISITED로 두고 

'''