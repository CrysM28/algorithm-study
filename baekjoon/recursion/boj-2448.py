# 2448. 별 찍기 - 11

def recursion(n, i, j):
    if n == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j+k] = '*'
        return
    
    n //= 2
    recursion(n, i, j)
    recursion(n, i+n, j-n)
    recursion(n, i+n, j+n)


N = int(input())
stars = [[' '] * (N*2-1) for _ in range(N)]

recursion(N, 0, N-1)

for star in stars:
    print(*star, sep='')

