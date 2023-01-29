# 2630. 색종이 만들기

WHITE = 0
BLUE = 1

def divide(n, i, j):
    global white_cnt, blue_cnt

    # print("===", n)
    # print(i, j)

    # 색 검사
    same = True
    color = paper[i][j]
    for x in range(i, i+n):
        for y in range(j, j+n):
            if color != paper[x][y]:
                same = False
                break

    # 전부 같은 색 
    if same:
        if color == WHITE:
            white_cnt += 1
        else:
            blue_cnt += 1
        return
    
    # 다른 색 섞임 (분할정복)
    half = n//2
    for di, dj in [(0,0), (half,0), (0,half), (half,half)]:
        ni = i+di
        nj = j+dj
        divide(half, ni, nj)



N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white_cnt, blue_cnt = 0, 0

divide(N, 0, 0)

print(white_cnt)
print(blue_cnt)


