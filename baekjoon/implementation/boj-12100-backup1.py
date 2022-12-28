# 12100. 2048 (Easy)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(*board, sep='\n')

# LRUD
#dir = ((0, -1), (0, 1), (1, 0), (-1, 0))
dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

def move_block_left():
    for i in range(N):
        for j in range(N-1):
            if board[i][j] == 0:
                board[i][j] = board[i][j+1]
                board[i][j+1] = 0
            elif board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0

def move_block_right():
    for i in range(N):
        for j in range(N-1,0,-1):
            if board[i][j] == 0:
                board[i][j] = board[i][j-1]
                board[i][j-1] = 0
            elif board[i][j] == board[i][j-1]:
                board[i][j] *= 2
                board[i][j-1] = 0

def move_block_up():
    for i in range(N-1):
        for j in range(N):
            if board[i][j] == 0:
                board[i][j] = board[i+1][j]
                board[i+1][j] = 0
            elif board[i][j] == board[i+1][j]:
                board[i][j] *= 2
                board[i+1][j] = 0

def move_block_down():
    for i in range(N-1,0,-1):
        for j in range(N):
            if board[i][j] == 0:
                board[i][j] = board[i-1][j]
                board[i-1][j] = 0
            elif board[i][j] == board[i-1][j]:
                board[i][j] *= 2
                board[i-1][j] = 0


move_block_left()
#move_block_down()

print(*board, sep='\n')
