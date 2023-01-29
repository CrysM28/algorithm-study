# 1992. 쿼드트리

def div(n, i, j):
    global qt

    bit = grid[i][j]

    for x in range(i, i+n):
        for y in range(j, j+n):

            # 분할정복
            if grid[x][y] != bit:
                qt += "("

                half = n//2
                for di, dj in [(0,0),(0,half),(half,0),(half,half)]:
                    ni = i+di
                    nj = j+dj
                    div(n//2, ni, nj)
                    
                qt += ")"

                return
    
    # 압축 (같은 경우) 
    qt += str(bit)


N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
qt = ""

div(N, 0, 0)
print(qt)
