# 게임 개발

N, M = map(int, input().split())
A, B, dir = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향: 북동남서
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


# 맵 표시 정보
LAND = 0
SEA = 1
VISITED = 2

grid[A][B] = VISITED
count = 1   # 방문한 칸의 수
turned = 0  # 회전 횟수

while True:
    # 반시계 회전
    dir -= 1
    nA = A + dx[dir%4]
    nB = B + dy[dir%4]

    # 가능하면 이동
    if nA >= 0 and nB >= 0 and nA < N and nB < N \
        and grid[nA][nB] == LAND:
        A = nA
        B = nB
        grid[nA][nB] = VISITED
        count += 1
        turned = 0

    # 이동 못했으면 회전만
    else:
        turned += 1

    # 네 방향 모두 막혀있으면 뒤로 이동
    if turned == 4:
        turned = 0
        nA = A - dx[dir%4]
        nB = B - dy[dir%4]
        if nA >= 0 and nB >= 0 and nA < N and nB < N \
            and grid[nA][nB] == LAND:
            A = nA
            B = nB
        # 이동할 수 없으면 정지
        else:
            break


    print("===")
    print(*grid, sep="\n")

print("===")
print(*grid, sep="\n")

print(count)