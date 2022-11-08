# 3:37~ 2:58 -> 40분
import copy


def solution(m, n, board):
    board = list(map(list, board))
    answer = 0
    pop = 10

    # 더 터질 게 없으면 루프 끝
    while pop != 0:
        new_board = copy.deepcopy(board)  # 임시 보드에 기록
        pop = 0

        # 2x2 찾기
        for i in range(m - 1):
            for j in range(n - 1):

                if board[i][j] != 0 and \
                    board[i][j] == board[i + 1][j] \
                    == board[i][j + 1] == board[i + 1][j + 1]:
                    # 터짐
                    pop += 1

                    # 블록 지우기
                    new_board[i][j] = 0
                    new_board[i + 1][j] = 0
                    new_board[i][j + 1] = 0
                    new_board[i + 1][j + 1] = 0

        # 빈 공간 메우기
        for j in range(n):
            for i in range(m - 1, -1, -1):
                while i+1 < m and new_board[i][j] != 0 and new_board[i+1][j] == 0:
                        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
                        i += 1

        board = copy.deepcopy(new_board)


    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1


    return answer

        #print(*board, sep='\n')
        #print(*new_board, sep='\n')

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(
    solution(6, 6,
             ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
