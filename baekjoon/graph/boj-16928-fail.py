# 16928. 뱀과 사다리 게임
## 우선순위 큐로는 왜 안될까요 아님 로직이 망했나

import heapq as h
import bisect
from collections import defaultdict

# 사다리 n, 뱀 m
n, m = map(int, input().split())

# 사다리, 뱀: 출발지점 기준 정렬
ladders = [list(map(int, input().split())) for _ in range(n)]
snakes = [list(map(int, input().split())) for _ in range(m)]
ladders.sort()
snakes.sort()

# 출발지점만 뽑은 리스트 (bisect용)
ladders_idx = [ladder[0] for ladder in ladders]
snakes_idx = [snake[0] for snake in snakes]


# 주사위 굴리는 횟수 계산하는 함수
def roll_dice(cur_pos, next_pos):
    dist = (next_pos - cur_pos)
    roll = 0
    snake_max = 0

    while dist > 0:
        for i in range(6, 0, -1):
            next_i = cur_pos + i
            
            # 주사위 굴리는 중간에 뱀 있으면 
            idx_l = bisect.bisect_left(snakes_idx, next_i)
            idx_r = bisect.bisect_right(snakes_idx, next_i)
            if idx_l != idx_r:
                if snake_max < snakes[idx_l][1]:
                    snake_max = snakes[idx_l][1]
                continue

            # 뱀 없으면
            dist -= i
            cur_pos += i
            roll += 1
            break

        # 다음 6칸이 모두 뱀이면 그나마 가장 큰 칸으로 이동
        else:
            roll += 1
            next_pos = snake_max
            break

    # next_pos 까지 가는데 굴린 주사위 수 roll
    return roll, next_pos


# 일부러 뱀 밟는 경우 굴리기
def roll_dice_snake(cur_pos, next_pos):
    dist = (next_pos - cur_pos)
    roll = 0

    while dist > 0:
        # 마지막 굴려서 목표뱀에 도달하기
        if dist <= 6:
            roll += 1
            break

        for i in range(6, 0, -1):
            next_i = cur_pos + i

            # 중간에 뱀 있으면 
            idx_l = bisect.bisect_left(snakes_idx, next_i)
            idx_r = bisect.bisect_right(snakes_idx, next_i)
            if idx_l != idx_r:
                continue
            # 뱀 없으면
            dist -= i
            cur_pos += i
            roll += 1
            break
        
        # 다음 6칸이 모두 뱀이면 cur_pos에서 그 뱀을 밟을 수 있는 경우는 없음
        else:
            roll = -1
            break

    return roll



# 우선순위 큐(최소힙) -> 주사위 최소로 굴린것부터 확인
q = [(0, 1)]
# {칸: 주사위 수} 최소값 갱신 안 되면 큐에 추가하지 않도록 관리
pos_min_dice = defaultdict(int)


while q:
    print(q)
    dice, pos = h.heappop(q)
    print(dice, pos)

    # 최초 도착할 때의 dice값이 최소
    if pos == 100:
        break

    # 현 위치보다 더 뒤에 있는 사다리, 뱀 확인
    ladder_start = bisect.bisect_left(ladders_idx, pos)
    snake_start = bisect.bisect_left(snakes_idx, pos)


    # 탈 수 있는 사다리 없으면 100까지 주사위
    if ladder_start == n:
        roll, arrived = roll_dice(pos, 100)
        # 만약 arrived가 100이 아니면 뱀 무조건 밟았다는 뜻 -> 다음 ladder 타고 처리
        #print("from ",pos," to 100")
        h.heappush(q, (dice + roll, arrived))

    # 있으면 사다리까지 주사위
    else:
        for ladder in ladders[ladder_start:]:
            cur_i, next_i = ladder

            # 너무 짧아서 주사위보다 사다리가 비효율적이면 그냥 100까지 굴리기
            if (next_i - pos) <= 6:
                roll, arrived = roll_dice(pos, 100)
                #print("too short, from ",pos," to 100")
                h.heappush(q, (dice + roll, arrived))
                continue

            # pos->cur_i까지 굴리는 주사위 수 roll
            # arrived == cur_i 면 next_i로 갈 수 있음
            roll, arrived = roll_dice(pos, cur_i)
            if arrived == cur_i:
                #print("can go ",pos," to", cur_i, "so adding ", dice+roll, next_i)
                h.heappush(q, (dice + roll, next_i))

            # arrived != cur_i면 arrived까지만 갈 수 있음
            # 무한반복 방지 -> 최소값 아니면 갱신 X
            elif arrived != cur_i:
                if not pos_min_dice[arrived] or pos_min_dice[arrived] > dice + roll:
                    #print("snake, can go ",pos," to", arrived, "so adding ", dice+roll, arrived)
                    pos_min_dice[arrived] = dice + roll
                    h.heappush(q, (dice + roll, arrived))



    # 뱀 밟아서 더 빨리 가는 경우도 있으니 확인
    if snake_start < m:
        for snake in snakes[snake_start:]:
            cur_i, next_i = snake
            roll = roll_dice_snake(pos, cur_i)

            # 밟을 수 없는 뱀 칸
            if roll == -1:
                continue

            # 최소값 아니면 갱신 X
            if not pos_min_dice[cur_i] or pos_min_dice[cur_i] > dice + roll:
                #print("adding snake from", cur_i, "to ", next_i, "with", roll)
                pos_min_dice[cur_i] = dice + roll
                h.heappush(q, (dice + roll, next_i))


print(dice)