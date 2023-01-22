# 1018. 체스판 다시 칠하기
## 588 -> 176로 축소 

def change_color(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE

def check(i, j):
    changed = [0, 0]
    color = WHITE

    for x in range(i, i+8):
        for y in range(j, j+8):
            if board[x][y] == color:
                changed[0] += 1
            else:
                changed[1] += 1
            color = change_color(color)
        color = change_color(color)
    
    return min(changed)


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

WHITE, BLACK = 'W', 'B'
min_change = int(1e9)

# 8x8 확인
for i in range(n - 7):
    for j in range(m - 7):
        cur_change = check(i, j)
        min_change = min(min_change, cur_change)

print(min_change)
