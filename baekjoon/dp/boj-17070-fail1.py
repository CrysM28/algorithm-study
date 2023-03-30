# 17070. 파이프 옮기기 1
## 문제만 보고는 브루트포스 구현 문제인줄 알았는데...

import copy

EMPTY = 0
WALL = 1

# 방향
HOR = 0     # 가로
VER = 1     # 세로
DIAG = 2    # 대각


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
pipe = [HOR, [0,0], [0,1]]
#print(*grid,sep='\n')

cnt = 0
def move():
    global cnt, pipe
    #print(pipe)

    r, c = pipe[2]

    if r == N-1 and c == N-1 and grid[r][c] == EMPTY:
        cnt += 1
        return



    if pipe[0] == HOR:
        # HOR move
        if c+1 < N and grid[r][c+1] == EMPTY:
            pipe = [HOR, [r, c], [r, c+1]]
            move()
        # DIAG move
        if r+1 < N and c+1 < N:
            for x, y in ((r+1, c), (r, c+1), (r+1, c+1)):
                if grid[x][y] != EMPTY:
                    break
            else:
                pipe = [DIAG, [r, c], [r+1, c+1]]
                move()
    
    elif pipe[0] == VER:
        # VER move
        if r+1 < N and grid[r+1][c] == EMPTY:
            pipe = [VER, [r, c], [r+1, c]]
            move()
        # DIAG move
        if r+1 < N and c+1 < N:
            for x, y in ((r+1, c), (r, c+1), (r+1, c+1)):
                if grid[x][y] != EMPTY:
                    break
            else:
                pipe = [DIAG, [r, c], [r+1, c+1]]
                move()
    
    elif pipe[0] == DIAG:
        # HOR move
        if c+1 < N and grid[r][c+1] == EMPTY:
            pipe = [HOR, [r, c], [r, c+1]]
            move()

        # VER move
        if r+1 < N and grid[r+1][c] == EMPTY:
            pipe = [VER, [r, c], [r+1, c]]
            move()
        # DIAG move
        if r+1 < N and c+1 < N:
            for x, y in ((r+1, c), (r, c+1), (r+1, c+1)):
                if grid[x][y] != EMPTY:
                    break
            else:
                pipe = [DIAG, [r, c], [r+1, c+1]]
                move()


move()
print(cnt)

# def dfs(house):
#     if house[N-1][N-1] == 2:
#         print("i am end")
#         print(*house,sep='\n')
#         return
#     pass

    # if dir == HOR:
    #     # HOR move
    #     if c+1 < N and grid[r][c+1] == EMPTY:
    #         dp[r][c+1] += 1
    #         pipe.append([HOR, r, c+1])
    #     # DIAG move
    #     if r+1 < N and c+1 < N:
    #         for x, y in ((r+1, c), (r, c+1), (r+1, c+1)):
    #             if grid[x][y] != EMPTY:
    #                 break
    #         else:
    #             dp[r+1][c+1] += 1
    #             pipe.append([DIAG, r+1, c+1])