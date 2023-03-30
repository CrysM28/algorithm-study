# 14499. 주사위 굴리기

N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

# 주사위 모양: (윗면, 북, 동, 바닥면, 남, 서) [위에서 본 기준]
dice = [0] * 6
new_dice = []

# 굴렸을 때 변화하는 인덱스
roll = [(),
        (5, 1, 0, 2, 4, 3),
        (2, 1, 3, 5, 4, 0),
        (4, 0, 2, 1, 3, 5),
        (1, 3, 2, 4, 0, 5)]

# 방향
dx = (0, 0, 0, -1, 1)
dy = (0, 1, -1, 0, 0)

for move in moves:
    # 범위 체크
    nx = x + dx[move]
    ny = y + dy[move]
    
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        continue
    
    # 굴리기
    for r in roll[move]:
        new_dice.append(dice[r])
    dice = new_dice[::]
    new_dice.clear()

    # 바닥 체크
    if grid[x][y] == 0:
        grid[x][y] = dice[3]
    else:
        dice[3] = grid[x][y]
        grid[x][y] = 0

    # 윗면 출력
    print(dice[0])

