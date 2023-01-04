# 3085. 사탕 게임
## 문제를 잘못 읽고 풀고 있었다
import copy, sys

sys.setrecursionlimit(10**4)

def update_max2(x, y):
    row = candies[x]
    col = []
    for a in range(N):
        col += candies[a][y]
    
    cnt1 = Counter(row).most_common(1)[0][1]
    cnt2 = Counter(col).most_common(1)[0][1]
    
    print(x, y, row, col, cnt1, cnt2)

    return max(cnt1, cnt2)

def update_max3():
    cur_max = 0
    for a in range(N):
        row = candies[a]
        col = []
        for b in range(N):
            col += candies[b][a]
        
        cnt1 = Counter(row).most_common(1)[0][1]
        cnt2 = Counter(col).most_common(1)[0][1]

        print(row, col, Counter(row).most_common(1), Counter(col).most_common(1))

        cur_max = max(cur_max, cnt1, cnt2)
    
    return cur_max

def update_max(x, y, color, grid, candy1):
    candy = 0

    if not (0 <= x < N and 0 <= y < N and grid[x][y] == color):
        return candy

    # 탐색 마친 곳은 값을 변경
    grid[x][y] = 'X'
    candy += 1

    candy += update_max(x+1, y, color, grid, candy)
    candy += update_max(x-1, y, color, grid, candy)
    candy += update_max(x, y+1, color, grid, candy)
    candy += update_max(x, y-1, color, grid, candy)

    return candy


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
                print("== i, j", i, j, ni, nj)
                candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]

                print(*candies, sep='\n')
                cur_candy1 = update_max(i, j, candies[i][j], copy.deepcopy(candies), 0)
                cur_candy2 = update_max(ni, nj, candies[ni][nj], copy.deepcopy(candies), 0)
                
                print(cur_candy1, cur_candy2, max_candy)
                max_candy = max(cur_candy1, cur_candy2, max_candy)

                candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]

print(max_candy)