# 12100. 2048 (Easy)
import copy

def move_block(board, d):
    global max_num

    di, dj = d
    range_i, range_j = board_range, board_range
    if di == 1:
        range_i = range_i[:-1]
    elif di == -1:
        range_i = range_i[::-1]
        range_i = range_i[:-1]
    if dj == 1:
        range_j = range_j[:-1]
    elif dj == -1:
        range_j = range_j[::-1]
        range_j = range_j[:-1]

    for i in range_i:
        for j in range_j:
            if board[i][j] == 0:
                board[i][j] = board[i+di][j+dj]
                board[i+di][j+dj] = 0
            elif board[i][j] == board[i+di][j+dj]:
                board[i][j] *= 2
                if board[i][j] > max_num:
                    max_num = board[i][j]
                board[i+di][j+dj] = 0

def play(board, cnt):
    #print("count", cnt)
    if cnt == 1:
        return
    
    for i in range(4):
        #print("dir", i)
        new_board = copy.deepcopy(board)
        move_block(new_board, dir[i])
        play(new_board, cnt+1)
        print("======== back", cnt, i)
        print(*new_board, sep='\n')



N = int(input())
init_board = [list(map(int, input().split())) for _ in range(N)]

# LRUD
dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
board_range = list(range(N))

max_num = 0
for b in init_board:
    max_num = max(max_num, max(b))

play(init_board, 0)

#print(*init_board, sep='\n')

print(max_num)