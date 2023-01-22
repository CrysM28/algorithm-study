# 18111. 마인크래프트

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_time = int(1e9)
max_ground = 0

for height in range(256, -1, -1):
    cur_time = 0
    blocks = B

    for i in range(N):
        for j in range(M):
            if ground[i][j] > height:
                diff = ground[i][j] - height
                blocks += diff
                cur_time += diff * 2
            elif ground[i][j] < height:
                diff = height - ground[i][j]
                blocks -= diff
                cur_time += diff
        
        # 최소시간 초과 시 조기종료
        if cur_time > min_time:
            break

    if blocks < 0:
        continue

    if min_time > cur_time:
        min_time = cur_time
        max_ground = height


print(min_time, max_ground)




