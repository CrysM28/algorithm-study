# 17136. 색종이 붙이기
from copy import deepcopy

def can_cover():
    return

def change_board():
    return

def backtrack(board, size, to_cover, left, used):
    if not to_cover:
        ans = used
        return



    left[size] -= 1




answer = 0

# 10x10 종이
grid = []
# 덮어야 하는 위치 (1)
need_cover = []
# 남은 종이
paper_left = [0, 5, 5, 5, 5, 5]


for i in range(10):
    line = list(map(int, input().split()))
    grid.append(line)

    for j in range(10):
        if line[j] == 1:
            need_cover.append([i, j])

# print(need_cover)



backtrack(grid, 5, need_cover, paper_left[:], 0)

print(paper_left)