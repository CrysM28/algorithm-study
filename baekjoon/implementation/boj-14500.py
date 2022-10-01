# 14500. 테트로미노

# 미리 만들어둔 모양
pieces = [
    # 1: 직선
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    # 2: 정사각형
    ((0, 0), (1, 0), (0, 1), (1, 1)),
    # 3: 지그재그
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (0, 2), (1, 0), (1, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),
    # 4: 볼록할 철
    ((0, 1), (1, 0), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    ((0, 0), (1, 0), (2, 0), (1, 1)),
    ((0, 1), (1, 0), (1, 1), (1, 2)),
    # 5: L자
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (0, 1)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 1), (1, 1), (2, 1), (2, 0)),
    ((0, 2), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    ((0, 0), (1, 0), (2, 0), (2, 1)),
]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

num_max = 0

# 시간복잡도 O(MN)
for j in range(M):
    for i in range(N):
        for piece in pieces:
            cur_sum = 0
            p1 = piece[0]
            p2 = piece[1]
            p3 = piece[2]
            p4 = piece[3]

            try:
                cur_sum += grid[i + p1[0]][j + p1[1]]
                cur_sum += grid[i + p2[0]][j + p2[1]]
                cur_sum += grid[i + p3[0]][j + p3[1]]
                cur_sum += grid[i + p4[0]][j + p4[1]]

                #print(piece, cur_sum, num_max)
                #print(grid[i + p1[0]][j + p1[1]], grid[i + p2[0]][j + p2[1]], grid[i + p3[0]][j + p3[1]], grid[i + p4[0]][j + p4[1]])
                num_max = max(num_max, cur_sum)

            # 범위 체크
            except IndexError:
                #print("outofrange", piece)
                continue

print(num_max)