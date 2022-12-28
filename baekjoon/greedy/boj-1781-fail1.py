# 1781. 컵라면
# 일단 브루트포스 -> 시간초과

import sys
sys.setrecursionlimit(10**5)

N = int(input())
cups = [list(map(int, input().split())) for _ in range(N)]

max_cup = 0
visited = [0] * N


def solve(time, cup):
    global max_cup
    if time > N:
        max_cup = max(max_cup, cup)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = time
            cur_cup = cup
            if cups[i][0] >= time:
                cur_cup += cups[i][1]
            solve(time+1, cur_cup)
            visited[i] = 0

solve(1, 0)

print(max_cup)