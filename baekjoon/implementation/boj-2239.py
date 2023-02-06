# 2239. 스도쿠

# 행, 열, 3x3 확인
def check(i, j, num):
    row = board[i]
    if num in row:
        return False
    
    col = [board[x][j] for x in range(9)]
    if num in col:
        return False

    ii, jj = i//3 * 3, j//3 * 3
    for x in range(ii, ii+3):
        for y in range(jj, jj+3):
            if board[x][y] == num:
                return False

    return True


# 백트래킹
def fill(cnt):
    if cnt == len(blank):
        for b in board:
            print(*b, sep='')
        exit(0)

    i, j = blank[cnt]

    for n in range(1,10):
        if check(i, j, n):
            board[i][j] = n
            fill(cnt+1)
            board[i][j] = 0



board = []  # 전체
blank = []  # 빈 칸 좌표

for i in range(9):
    data = list(map(int, input()))
    board.append(data)
    for j in range(9):
        if data[j] == 0:
            blank.append([i, j])


fill(0)

