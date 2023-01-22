# 1018. 체스판 다시 칠하기

import copy


def check_board(max_i, max_j, start):
    cur_board = copy.deepcopy(board)      # work with copied board
    changed = 0

    # check all squares in board
    for i in range(max_i - 8, max_i):
        for j in range(max_j - 8, max_j):

            # set start color (left-uppermost square)
            if i == max_i - 8 and j == max_j - 8:
                if cur_board[i][j] != start:
                    changed += 1
                    cur_board[i][j] = start

            square = cur_board[i][j]
            if square == white: other_sq = black
            else: other_sq = white

            # check right
            if j + 1 < max_j and cur_board[i][j + 1] == square:
                cur_board[i][j + 1] = other_sq
                changed += 1

            # check down
            if i + 1 < max_i and cur_board[i + 1][j] == square:
                cur_board[i + 1][j] = other_sq
                changed += 1

    return changed


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

white, black = 'W', 'B'
min_change = 1000000

# change board range
for i in range(8, n + 1):
    for j in range(8, m + 1):
        # check for each when left-uppermost is black/white
        changed_black = check_board(i, j, black)
        changed_white = check_board(i, j, white)
        min_change = min(changed_black, changed_white, min_change)

print(min_change)

#print(*board, sep='\n')
