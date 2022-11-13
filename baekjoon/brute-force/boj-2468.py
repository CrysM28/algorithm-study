# 2468. 안전영역
import copy
import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    if i < 0 or i >= N or \
        j < 0 or j >= N or \
            grid[i][j] <= rain:
            return

    grid[i][j] = rain-1

    dfs(i-1, j)
    dfs(i+1, j) 
    dfs(i, j-1) 
    dfs(i, j+1) 


N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

max_group = 1

for rain in range(1, 101):
    grid = copy.deepcopy(land)
    group = 0 

    for h in range(N):
        for w in range(N):
            if grid[h][w] > rain:
                dfs(h, w)
                group += 1 

    if group == 0:
        break

    max_group = max(max_group, group)


print(max_group)




'''
비의 양에 따라 물에 잠기지 않는 안전한 영역의 개수

하나도 안 잠기는 경우
일단 1부터 100까지 다 돌린다고 치고





'''