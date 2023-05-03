# 23291. 어항 정리
## 252ms
from collections import deque
import copy

# 물고기 수 조정 1
## 최소 물고기 수 +1
def add_one_fish(min_f_num):
    f = fish[0]
    for i in range(N):
        if f[i] == min_f_num:
            f[i] += 1


# 어항 정리 1
## 2층 이상의 어항 시계 90도 회전 후 다시 쌓기 반복
def magic_1():

    # 1) 초기 어항 쌓기: 맨 왼쪽을 바로 옆 위에 쌓기
    a = fish[0].popleft()
    fish.appendleft(deque([a]))

    ## 더 못 쌓을때까지 반복
    while True:
        fly = []                    # 공중부양할 어항
        n = len(fish)               # 공중부양할 어항 (세로 길이)
        m = len(fish[0])            # 공중부양할 어항 (가로 길이)
        left_m = len(fish[-1]) - m  # 남은 어항

        # print("---")
        # print(fish)
        # print(m, left_m)

        ## 쌓을 수 있는지 미리 확인
        if n > left_m:
            return

        # 2) 공중부양할 어항 분리
        for i in range(n):
            tmp = []
            for _ in range(m):
                tmp.append(fish[i].popleft())
            fly.append(tmp)
        
        ## 빈 어항 치우기
        while not fish[0]:
            fish.popleft()

        # 3) 공중부양 어항 시계방향 90도 회전
        fly = rotate_cw_90(fly)

        # 4) 위에 얹기
        for f in fly[::-1]:
            fish.appendleft(deque(f))


# 물고기 수 조정 2
## 인접 어항 물고기 수에 따라 나눠주기
def move_fish():
    
    ## 물고기 계산
    def redistribute_fish(i, j, ni, nj):
        if (ni, nj) not in visited:
            # 방문 표시
            #print("lets go", ni, nj)
            #visited.add((ni, nj))
            queue.append((ni, nj))

            # 계산
            v = fish[i][j]
            v_down = fish[ni][nj]

            if v_down > v:
                d = (v_down - v) // 5
                tmp_fish[i][j] += d
                tmp_fish[ni][nj] -= d
            else:
                d = (v - v_down) // 5
                tmp_fish[i][j] -= d
                tmp_fish[ni][nj] += d


    tmp_fish = copy.deepcopy(fish)

    visited = set([])
    queue = deque([(0,0)])
    row = len(fish)
    short_col = len(fish[0])
    long_col = len(fish[-1])

    while queue:
        r, c = queue.popleft()
        #print(r, c, fish[r][c])

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # 아래 (세로 이동)
        if r+1 < row:
            redistribute_fish(r,c,r+1,c)

        # 오른쪽 (가로 이동)
        if (r == row-1 and c+1 < long_col) or c+1 < short_col:
            redistribute_fish(r,c,r,c+1)

        #print(tmp_fish)
    
    return tmp_fish


# 일렬화
def serialize():
    f_list = []
    row = len(fish)
    col = len(fish[0])

    # 겹친 부분
    for c in range(col):
        for r in range(1, row+1):
            f_list.append(fish[-r][c])

    # 나머지 꼬리
    f_list += list(fish[-1])[c+1:]

    return f_list

# 어항 정리 2
def magic_2():
    new_list = []

    # 1) 절반 접기 1
    n = len(fish) // 2
    left_half = fish[:n]
    right_half = fish[n:]

    ## 위에 얹는 것 180도 회전
    new_list.append(left_half[::-1])
    new_list.append(right_half)


    # 2) 절반 접기 2
    row = len(new_list)
    col = n // 2

    left_half = [new_list[i][:col] for i in range((row//2) +1)]
    right_half = [new_list[i][col:] for i in range((row//2)-1, row)]

    ## 위에 얹는 것 180도 회전 (90도 회전 2번)
    left_half = rotate_cw_90(left_half)
    left_half = rotate_cw_90(left_half)

    new_list = left_half + right_half

    return new_list



## 배열 회전
def rotate_cw_90(my_list):
    return list(map(list, zip(*my_list[::-1])))




# 어항 수, 목표 물고기 수 최대-최소 차이
N, K = map(int, input().split())

# 어항
fish = deque([])
fish.append(deque(map(int, input().split())))

# 물고기 수 최대-최소 차이
max_fish_num = max(fish[0])
min_fish_num = min(fish[0])
ans = max(fish[0]) - min(fish[0])

cnt = 0

while ans > K:
    cnt += 1

    # 어항 정리
    add_one_fish(min_fish_num)
    magic_1()
    fish = move_fish()
    fish = serialize()
    fish = magic_2()
    fish = move_fish()
    fish_list = serialize()

    # 최대-최소 차이 계산
    fish = deque()
    fish.append(deque(fish_list))
    max_fish_num = max(fish[0])
    min_fish_num = min(fish[0])
    ans = max(fish[0]) - min(fish[0])

print(cnt)



# while ans > K:

#     cnt += 1
#     print("------------------ cnt", cnt)

#     print("==1")
#     add_one_fish(min_fish_num)
#     print(fish)

#     print("==2")
#     magic_1()
#     print(fish)

#     print("==3")
#     fish = move_fish()
#     print(fish)

#     print("==4")
#     fish = serialize()
#     print(fish)

#     print("==5")
#     fish = magic_2()
#     print(fish)

#     print("==6")
#     fish = move_fish()
#     print(fish)


#     print("==7")
#     fish_list = serialize()
#     print(fish_list)


#     # 최대-최소 차이 계산
#     fish = deque()
#     fish.append(deque(fish_list))
#     max_fish_num = max(fish[0])
#     min_fish_num = min(fish[0])
#     ans = max(fish[0]) - min(fish[0])


# print(cnt)


# print("==1")
# add_one_fish(min_fish_num)
# print(fish)

# print("==2")
# magic_1()
# print(fish)

# print("==3")
# fish = move_fish()
# print(fish)

# print("==4")
# fish = serialize()
# print(fish)

# print("==5")
# fish = magic_2()
# print(fish)

# print("==6")
# fish = move_fish()
# print(fish)


# print("==7")
# fish_list = serialize()
# print(fish_list)

