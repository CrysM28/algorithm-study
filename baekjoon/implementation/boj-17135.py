# 17135. 캐슬 디펜스
import copy
from collections import deque
BLANK = 0
ENEMY = 1

N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
org_grid = copy.deepcopy(grid)

enemy_list = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == ENEMY:
            enemy_list.append([i,j])

max_cnt = 0

archers = []
def get_archers():
    global max_cnt, grid
    if len(archers) == 3:
        grid = copy.deepcopy(org_grid)
        cur_cnt = play_game(archers, enemy_list)
        #print(archers, cur_cnt)
        max_cnt = max(max_cnt, cur_cnt)
        return
    
    for i in range(M):
        if not archers or i > archers[-1]:
            archers.append(i)
            get_archers()
            archers.pop()


def play_game(archers, enemy_list):
    cnt = 0
    while enemy_list:
        # 죽는 거 찾아내기
        cur_dead = find_killed_enemies(archers)
        #print("killed")
        #print(cur_dead)

        new_enemy_list = []
        #killed = []
        #all_blank = True
        for i in range(N-1, -1, -1):
            for j in range(M):
                if grid[i][j] == ENEMY and [i, j] in cur_dead:
                    cnt += 1

                grid[i][j] = BLANK
                if i != 0 and grid[i-1][j] == ENEMY and [i-1, j] not in cur_dead:
                    new_enemy_list.append([i, j])
                    grid[i][j] = ENEMY
                
        #print("===")
        #print(*grid,sep='\n')


        enemy_list = new_enemy_list
        # print("left")
        # print(enemy_list)
        # print("===")
        # print(*grid,sep='\n')
        #print(cnt)
    return cnt


def find_killed_enemies(archers):
    di = (0, 0, -1)
    dj = (-1, 1, 0)

    dead_enemies = []

    # 궁수마다 계산
    for a in archers:
        visited = [[False]*M for _ in range(N)]
        queue = deque([[N, a]])
        next_queue = []
        dist = 1
        cur_enemies = []

        while queue:
            i, j = queue.popleft()
            #print(i, j, dist)

            if dist > D:
                break

            for x in range(3):
                ni = i + di[x]
                nj = j + dj[x]

                if ni == N and x == 2:
                    ni -= 1

                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                    next_queue.append([ni, nj])
                    visited[ni][nj] = True

                    if grid[ni][nj] == ENEMY:
                        cur_enemies.append([ni, nj])

            if not queue:
                #print(next_queue)
                #print(cur_enemies)
                if cur_enemies:
                    cur_enemies.sort(key=lambda x:x[1])
                    #print(cur_enemies)
                    dead_enemies.append(cur_enemies[0])
                    break

                queue = deque(next_queue)
                next_queue.clear()

                dist += 1


    return dead_enemies



get_archers()

#archers = [0,2,4]
#play_game(archers, enemy_list)

print(max_cnt)


        # new_enemy_list = []
        # for e in enemy_list[::-1]:
        #     i, j = e
        #     if e in cur_dead:
        #         grid[i][j] = BLANK
        #         cnt += 1
        #     elif i+1 < N:
        #         new_enemy_list.append([i+1, j])
        #         grid[i][j] = BLANK
        #         grid[i+1][j] = ENEMY
        # enemy_list = new_enemy_list