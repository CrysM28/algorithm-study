# 상하좌우

N = int(input())
moves = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for m in moves:
    # 이동 후 좌표 구하기
    i = move_types.index(m)
    nx = x + dx[i]
    ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)