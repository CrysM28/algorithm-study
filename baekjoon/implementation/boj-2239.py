# 2239. 스도쿠

sudoku = [list(map(int, input())) for _ in range(9)]

def find_square(i, j):
    
    sq = j//3 + (i//3)*3 
    print(sq)


def check(i, j):
    val = sudoku[i][j]

    row = sudoku[i][:j] + sudoku[i][j+1:]
    if val in row:
        return False
    
    col = []
    for x in range(9):
        if x == i: continue
        col.append(sudoku[x][j])
    if val in col:
        return False

    box = []
    find_square(i, j)
    if val in box:
        return False
    
    return True


def fill(i, j):
    for t in range(1,9):
        sudoku[i][j] = t
        if check(i, j):
            return



for ii in range(9):
    for jj in range(9):
        if sudoku[ii][jj] == 0:
            fill(ii, jj)


#print(check(3, 4))

print(*sudoku, sep='\n')
