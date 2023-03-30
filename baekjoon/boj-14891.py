# 14891. 톱니바퀴

# 톱니바퀴
gears = [[]] + [list(map(int, input())) for _ in range(4)]

# 회전 함수
def rotate(gear_no, dir):
    new_gear = [0] * 8
    for i in range(8):
        new_gear[i] = gears[gear_no][(i-dir)%8]
    return new_gear

# 회전시키기
K = int(input())
for _ in range(K):
    cur_gear, cur_dir = map(int, input().split())

    # 회전 여부, 방향 관리
    is_rotate = [False] * 5
    rotate_dir = [0] * 5
    is_rotate[cur_gear] = True
    rotate_dir[cur_gear] = cur_dir
    
    # 왼쪽 회전여부 확인
    left_gear = cur_gear - 1
    while left_gear > 0:
        # 다른 극: 반대방향 회전, 같은 극: 회전 X
        if gears[left_gear][2] != gears[left_gear+1][6]:
            is_rotate[left_gear] = True
            rotate_dir[left_gear] = -rotate_dir[left_gear+1]
        else:
            break
        left_gear -= 1
    
    # 오른쪽 회전여부 확인
    right_gear = cur_gear + 1
    while right_gear < 5:
        if gears[right_gear-1][2] != gears[right_gear][6]:
            is_rotate[right_gear] = True
            rotate_dir[right_gear] = -rotate_dir[right_gear-1]
        else:
            break
        right_gear += 1
    
    # 회전시키기
    for i in range(1, 5):
        if is_rotate[i]:
            gears[i] = rotate(i, rotate_dir[i])
    
    # debug
    #print(*gears,sep='\n')
    #print(is_rotate)
    #print(rotate_dir)


score = 0
for i in range(1, 5):
    if gears[i][0]:
        score += 2 ** (i-1)

print(score)


