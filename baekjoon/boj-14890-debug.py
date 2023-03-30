# 14890. 경사로

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def eval_path():
    cnt = 0

    for i in range(N):
        road = grid[i]
        cur_num, cur_cnt = road[0], 1
        j = 0
        can_go = True
        
        print('==', i)
        print(road)

        while can_go and j < N-1:
            print(j)
            #prev_num = cur_num
            next_num = road[j+1]

            # 같음
            if cur_num == next_num:
                print("same")
                j += 1
                cur_cnt += 1

            # 높아짐
            elif cur_num + 1 == next_num:
                print("high")
                if cur_cnt >= L:
                    j += 1
                    cur_num = next_num
                    cur_cnt = 1
                else:
                    can_go = False

            # 낮아짐
            elif cur_num - 1 == next_num:
                print("low")
                for next in range(2, L+1):
                    #print(j, next, cur_num, road[j+next])
                    if j+next >= N or road[j+next] != next_num:
                        can_go = False
                        break
                
                j += L
                if j < N:
                    cur_num = road[j]
                    cur_cnt = 0

            else:
                can_go = False

        if can_go:
            cnt += 1
        
        print(can_go)

    return cnt


count = eval_path()
print(count)
grid = list(zip(*grid[::-1]))
count += eval_path()

print(count)

