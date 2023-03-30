# 13460. 구슬 탈출 2
di = (0, 0, -1, 1)
dj = (-1, 1, 0, 0)


def turn(dir, i, j, color):
    while 0 <= i < N and 0 <= j < M:
        if board[i][j] == 'O':
            return (True, i, j)
        elif board[i][j] == '#':
            i -= di[dir]
            j -= dj[dir]
            board[i][j] = color
            return (False, i, j)
        
        i += di[dir]
        j += dj[dir]


def move(cnt, is_solved):
    global ri, rj, bi, bj
    print(cnt)

    if is_solved:
        print(cnt)
        exit(0)
    
    if cnt == 10:
        print(-1)
        exit(0)
    
    org_ri, org_rj = ri, rj
    for direction in range(4):
        is_red_exit, new_ri, new_rj = turn(direction, ri, rj, 'R')
        board[ri][rj] = '.'
        board[new_ri][new_rj] = 'R'
        ri, rj = new_ri, new_rj

        is_blue_exit, new_bi, new_bj = turn(direction, bi, bj, 'B')
        board[bi][bj] = '.'
        board[new_bi][new_bj] = 'B'
        bi, bj = new_bi, new_bj

        print(is_red_exit, is_blue_exit)
        print("==")
        print(*board, sep='\n')
        print("==")

        if not is_blue_exit:
            if is_red_exit:
                move(cnt+1, True)
            else:
                move(cnt+1, False)

        ri, rj = org_ri, org_rj

        # board[ri][rj] = 'R'
        # board[new_ri][new_rj] = '.'
        # board[bi][bj] = '.'
        # board[new_bi][new_bj] = 'B'



N, M = map(int, input().split())
board = []
ri, rj = 0, 0
bi, bj = 0, 0

for i in range(N):
    data = list(input())
    board.append(data)
    if 'R' in data:
        ri = i
        rj = data.index('R')
    if 'B' in data:
        bi = i
        bj = data.index('B')




move(0, False)
#turn(3, bi, bj, 'B')
print(*board, sep='\n')


# 13460. 구슬 탈출 2
di = (0, 0, -1, 1)
dj = (-1, 1, 0, 0)


def turn(dir, i, j, color):
    while 0 <= i < N and 0 <= j < M:
        if board[i][j] == 'O':
            return (True, i, j)
        elif board[i][j] == '#':
            i -= di[dir]
            j -= dj[dir]
            board[i][j] = color
            return (False, i, j)
        
        i += di[dir]
        j += dj[dir]


def move(cnt, ri, rj, bi, bj):
    print(cnt)

    # if is_solved:
    #     print(cnt)
    #     exit(0)
    
    if cnt == 10:
        print(-1)
        return
    
    #org_ri, org_rj = ri, rj
    for direction in range(4):
        print("==", direction)
        # try
        is_red_exit, new_ri, new_rj = turn(direction, ri, rj, 'R')
        is_blue_exit, new_bi, new_bj = turn(direction, bi, bj, 'B')

        print(is_red_exit, is_blue_exit)
        print(*board, sep='\n')
        print("==")

        if (ri, rj, bi, bj) == (new_ri, new_rj, new_bi, new_bj):
            print("same")
            continue


        # check
        if not is_blue_exit:
            if is_red_exit:
                print(cnt)
                exit(0)
            else:
                move(cnt+1, new_ri, new_rj, new_bi, new_bj)

        # backtrack (rewind)
        #ri, rj = org_ri, org_rj

        # board[ri][rj] = 'R'
        # board[new_ri][new_rj] = '.'
        # board[bi][bj] = '.'
        # board[new_bi][new_bj] = 'B'



N, M = map(int, input().split())
board = []
red_i, red_j = 0, 0
blue_i, blue_j = 0, 0

for i in range(N):
    data = list(input())
    board.append(data)
    if 'R' in data:
        red_i = i
        red_j = data.index('R')
    if 'B' in data:
        blue_i = i
        blue_j = data.index('B')


move(0, red_i, red_j, blue_i, blue_j)
#print(*board, sep='\n')

print("failed, -1")

# 13460. 구슬 탈출 2
di = (0, 0, -1, 1)
dj = (-1, 1, 0, 0)


def turn(dir, i, j, color):
    while 0 <= i < N and 0 <= j < M:
        if board[i][j] == 'O':
            return (True, i, j)
        elif board[i][j] in ['#', 'R', 'B']:
            i -= di[dir]
            j -= dj[dir]
            board[i][j] = color
            return (False, i, j)
        
        i += di[dir]
        j += dj[dir]


def move(cnt, ri, rj, bi, bj):
    global min_cnt
    #print(cnt)

    # if is_solved:
    #     print(cnt)
    #     exit(0)
    
    if cnt == 10:
        print(-1)
        return
    
    for direction in range(4):
        print("cnt", cnt, "dir", direction)
        # try
        board[ri][rj], board[bi][bj] = '.', '.'
        is_red_exit, new_ri, new_rj = turn(direction, ri, rj, 'R')
        is_blue_exit, new_bi, new_bj = turn(direction, bi, bj, 'B')
        board[new_ri][new_rj], board[new_bi][new_bj] = 'R', 'B'

        #print(*board, sep='\n')


        # check
        if (ri, rj, bi, bj) == (new_ri, new_rj, new_bi, new_bj):
            #print("same")
            continue

        if not is_blue_exit:
            if is_red_exit:
                print("== success", cnt, min_cnt)
                min_cnt = min(min_cnt, cnt)
            else:
                move(cnt+1, new_ri, new_rj, new_bi, new_bj)

        # backtrack (rewind)
        board[ri][rj], board[bi][bj] = 'R', 'B'
        board[new_ri][new_rj], board[new_bi][new_bj] = '.', '.'




N, M = map(int, input().split())
board = []
red_i, red_j = 0, 0
blue_i, blue_j = 0, 0

min_cnt = 10

for i in range(N):
    data = list(input())
    board.append(data)
    if 'R' in data:
        red_i = i
        red_j = data.index('R')
    if 'B' in data:
        blue_i = i
        blue_j = data.index('B')


move(0, red_i, red_j, blue_i, blue_j)
#print(*board, sep='\n')

print(min_cnt)
###################
def move(cnt, ri, rj, bi, bj):
    global min_cnt
    #print(cnt)

    # if is_solved:
    #     print(cnt)
    #     exit(0)
    
    if cnt == 10:
        print(-1)
        return
    
    for direction in range(4):
        print("cnt", cnt, "dir", direction)
        # try
        board[ri][rj], board[bi][bj] = '.', '.'
        is_red_exit, new_ri, new_rj = turn(direction, ri, rj, 'R')
        is_blue_exit, new_bi, new_bj = turn(direction, bi, bj, 'B')
        board[new_ri][new_rj], board[new_bi][new_bj] = 'R', 'B'

        #print(*board, sep='\n')


        # check
        if (ri, rj, bi, bj) == (new_ri, new_rj, new_bi, new_bj):
            #print("same")
            continue

        if not is_blue_exit:
            if is_red_exit:
                print("== success", cnt, min_cnt)
                min_cnt = min(min_cnt, cnt)
            else:
                move(cnt+1, new_ri, new_rj, new_bi, new_bj)

        # backtrack (rewind)
        board[ri][rj], board[bi][bj] = 'R', 'B'
        board[new_ri][new_rj], board[new_bi][new_bj] = '.', '.'

def turn(d, i, j):
    cnt = 0
    while 0 <= i < N and 0 <= j < M:
        if board[i][j] == 'O':
            return (i, j, cnt)
        elif board[i][j] == '#':
            i -= di[d]
            j -= dj[d]
            return (i, j, cnt-1)
        
        i += di[d]
        j += dj[d]
        cnt += 1

print("== dir", dir)
print("red", nri, nrj, rcnt)
print("blue", nbi, nbj, bcnt)
