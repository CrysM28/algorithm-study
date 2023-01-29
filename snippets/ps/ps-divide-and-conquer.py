# DIV 등분으로 나눠서 같은 정사각형의 개수를 확인하는 분할정복 문제

DIV = 3

def divide(n, i, j):
    # 색 검사
    color = paper[i][j]
    for x in range(i, i+n):
        for y in range(j, j+n):
            # 다른 색 섞임 (분할정복)
            if color != paper[x][y]:
                for ni in range(i, i+n, n//DIV):
                    for nj in range(j, j+n, n//DIV):
                        divide(n//DIV, ni, nj)
                return

    # 전부 같은 색 
    idx = color + 1
    ans[idx] += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * DIV

divide(N, 0, 0)
print(*ans, sep="\n")
