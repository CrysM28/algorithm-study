# 17144. 미세먼지 안녕!

R, C, T = map(int, input().split())

# 공청기 위쪽
cleaner_up = []
di_up = (0, -1, 0, 1)
dj_up = (1, 0, -1, 0)

# 공청기 아래쪽
cleaner_down = []
di_down = (0, 1, 0, -1)
dj_down = (1, 0, -1, 0)


# 공청기 작동
def run_cleaner(di, dj, cur_cleaner):
    prev = 0
    i, j = cur_cleaner

    for x in range(4):
        while True:
            ni = i + di[x]
            nj = j + dj[x]

            if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1):
                break

            cur = grid[ni][nj]
            grid[ni][nj] = prev
            prev = cur

            i = ni
            j = nj


# 미세먼지 정보 (위치(i, j), 값(/5))
dust = []

# 방 격자
#grid = [list(map(int, input().split())) for _ in range(R)]
grid = []

for i in range(R):
    line = list(map(int, input().split()))
    grid.append(line)

    for j in range(C):
        if line[j] == -1:
            if not cleaner_up:
                cleaner_up = [i, j]
            else:
                cleaner_down = [i, j]
        elif line[j] > 0:
            dust.append([i, j, line[j]//5])

# print(*grid, sep = "\n")
# print(dust)


for _ in range(T):
    # 1. 확산
    while dust:
        i, j, d = dust.pop()

        for x in range(4):
            ni = i + di_down[x]
            nj = j + dj_down[x]
            
            if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1:
                grid[ni][nj] += d
                grid[i][j] -= d


    # 2. 이동 (공청기 가동)
    ## 위쪽 (반시계방향)
    run_cleaner(di_up, dj_up, cleaner_up)
    ## 아래쪽 (시계방향)
    run_cleaner(di_down, dj_down, cleaner_down)


    # 3. 새로운 먼지 큐 추가
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                dust.append([i, j, grid[i][j]//5])


# print(*grid, sep = "\n")

# 미세먼지 합 계산
answer = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] > 0:
            answer += grid[i][j]

print(answer)



    # ## 위쪽 (반시계방향)
    # prev = 0
    # i, j = cleaner_up

    # for x in range(4):
    #     while True:
    #         ni = i + di_up[x]
    #         nj = j + dj_up[x]

    #         if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1):
    #             break

    #         cur = grid[ni][nj]
    #         grid[ni][nj] = prev
    #         prev = cur

    #         i = ni
    #         j = nj

    # ## 아래쪽 (시계방향)
    # prev = 0
    # i, j = cleaner_down

    # for x in range(4):
    #     while True:
    #         ni = i + di_down[x]
    #         nj = j + dj_down[x]

    #         if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1):
    #             break

    #         cur = grid[ni][nj]
    #         grid[ni][nj] = prev
    #         prev = cur

    #         i = ni
    #         j = nj
