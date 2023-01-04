# 3085. 사탕 게임

def update_max():
    cur_max = 0

    for x in range(N):
        row_cnt = 1
        row_before = 'X'
        for y in range(N):
            if candies[x][y] == row_before:
                row_cnt += 1
            else:
                row_before = candies[x][y]
                cur_max = max(cur_max, row_cnt)
                row_cnt = 1
        cur_max = max(cur_max, row_cnt)

    for y in range(N):
        col_cnt = 1
        col_before = 'X'
        for x in range(N):
            #print(x, y, col_before, candies[x][y])
            if candies[x][y] == col_before:
                col_cnt += 1
            else:
                col_before = candies[x][y]
                cur_max = max(cur_max, col_cnt)
                col_cnt = 1
        cur_max = max(cur_max, col_cnt)

    return cur_max


N = int(input())
candies = [list(input()) for _ in range(N)]

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)
max_candy = 0

for i in range(N):
    for j in range(N):
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            
            if candies[i][j] != candies[ni][nj]:
                candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]                
                max_candy = max(max_candy, update_max())
                candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]
            
            if max_candy == N:
                break


print(max_candy)