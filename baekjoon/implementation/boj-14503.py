# 14503. 로봇 청소기


EMPTY = 0
WALL = 1
CLEANED = 2

# 세로크기 n, 가로크기 m
n, m = map(int, input().split())
# 좌표 (r,c), 방향 d
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]


# 좌표: 북동남서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 청소한 영역 개수
clean_num = 0


# 왼쪽 방향으로 돌며 주위 확인
def rotate_and_clean():
    global r, c, d
    
    for i in range(1, 5):
        # 회전 방향
        nd = (d - i) % 4
        # 회전 후 이동한 좌표
        nr = r + dr[nd] 
        nc = c + dc[nd]

        # 이동 가능하면 청소하고 True 반환
        if nr >= 0 and nr < n and nc >= 0 and nc < m and room[nr][nc] == EMPTY:
            #print("cleaned", r,c, "nexT", nr, nc, nd)
            r = nr
            c = nc
            d = nd
            return True
    
    # 이동 못했으면 False 반환
    return False


# 안 될때까지 청소
cant_move = False
while True:
    # 현재 위치 청소
    room[r][c] = CLEANED
    clean_num += 1

    # 청소 못했으면 한칸 후진하고 다시 주위 확인
    while not rotate_and_clean():
        # 한칸 후진
        r += dr[d-2] 
        c += dc[d-2]

        # 범위 벗어나면 중지
        if r < 0 or r >= n or c < 0 or c >= m or room[r][c] == WALL:
            cant_move = True
            break

    # 더 움직일 수 없으니 중지
    if cant_move:
        break

    # print(clean_num)
    # print(*room, sep='\n')



print(clean_num)
#print(*room, sep='\n')
