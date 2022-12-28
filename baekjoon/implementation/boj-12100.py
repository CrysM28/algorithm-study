# 12100. 2048 (Easy)
import copy

def move_block_left(board):
    for i in range(N):
        ptr = 0
        for j in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][ptr] == 0:
                    board[i][ptr] = tmp
                elif board[i][ptr] == tmp:
                    board[i][ptr] *= 2
                    ptr += 1
                else:
                    ptr += 1
                    board[i][ptr] = tmp
    return board
   
def move_block_right(board):
    for i in range(N):
        ptr = N-1
        for j in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][ptr] == 0:
                    board[i][ptr] = tmp
                elif board[i][ptr] == tmp:
                    board[i][ptr] *= 2
                    ptr -= 1
                else:
                    ptr -= 1
                    board[i][ptr] = tmp
    return board

def move_block_up(board):
    for j in range(N):
        ptr = 0
        for i in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[ptr][j] == 0:
                    board[ptr][j] = tmp
                elif board[ptr][j] == tmp:
                    board[ptr][j] *= 2
                    ptr += 1
                else:
                    ptr += 1
                    board[ptr][j] = tmp
    return board

def move_block_down(board):
    for j in range(N):
        ptr = N-1
        for i in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[ptr][j] == 0:
                    board[ptr][j] = tmp
                elif board[ptr][j] == tmp:
                    board[ptr][j] *= 2
                    ptr -= 1
                else:
                    ptr -= 1
                    board[ptr][j] = tmp
    return board


def play(board, cnt):
    global max_num
    if cnt == 5:
        max_num = max(max_num, max(map(max, board)))
        return
    
    for i in range(4):
        new_board = copy.deepcopy(board)
        if i == 0:
            play(move_block_left(new_board), cnt+1)
        elif i == 1:
            play(move_block_right(new_board), cnt+1)
        elif i == 2:
            play(move_block_up(new_board), cnt+1)
        else:
            play(move_block_down(new_board), cnt+1)

    #print(*new_board, sep='\n')

max_num = 0
N = int(input())
init_board = [list(map(int, input().split())) for _ in range(N)]

play(init_board, 0)

print(max_num)