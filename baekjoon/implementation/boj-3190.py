# 3190. 뱀

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
apples = [list(map(int, input().split())) for _ in range(k)]  # 사과의 위치
l = int(input())  # 뱀의 방향 변환 횟수
moves = [list(input().split()) for _ in range(l)]  # 뱀의 이동경로 (L: 왼, D: 오)

time = 0  # 게임이 끝나는 시간
snake = []  # 뱀이 차지하는 공간
snake_len = 1  # 뱀의 길이
pos = [1, 1]  # 뱀의 현 위치 (i,j)

# 뱀 진행방향
dir = 0  # 0R 1D 2L 3U
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
## 초기화
x = int(moves[0][0])  # 방향 바뀌는 시간
c = moves[0][1]  # 바뀌는 방향
moves.pop(0)


# 게임 진행
while True:
    # 초 세기
    time += 1

    ## 1. 먼저 뱀은 몸길이를 늘려 머리를 위치시킨다
    # 현 방향으로 이동
    pos[0] += di[dir]
    pos[1] += dj[dir]
    snake.append(pos[:])
    
    # 벽인지 확인 -> 게임 종료
    if pos[0] < 1 or pos[0] > n or pos[1] < 1 or pos[1] > n:
        break

    # 자기 꼬리인지 확인 (머리 제외) -> 게임 종료
    if pos in snake[:snake_len - 2]:
        break


    ## 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다
    # 사과 먹었는지 확인 -> 사과 삭제, 꼬리 길이 증가
    if pos in apples:
        apples.remove(pos)
        snake_len += 1


    ## 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
    # 보드상 뱀 위치 확인 -> 꼬리 길이 맞게 조정
    while len(snake) > snake_len:
        snake.pop(0)


    ## 방향 조정 -> c에 명시된 방향으로
    if x == time:
        if c == 'D':
            dir = (dir + 1) % 4
        elif c == 'L':
            dir = (dir + 3) % 4

        # 움직일 방향 남아있으면 다음 바뀔 시간, 방향 저장
        if moves:
            x, c = int(moves[0][0]), moves[0][1]
            moves.pop(0)

# 게임 종료 시간
print(time)
