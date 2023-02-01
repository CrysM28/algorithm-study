# 16928. 뱀과 사다리 게임
from collections import deque

N, M = map(int, input().split())
ladders_list = [list(map(int, input().split())) for _ in range(N)]
snakes_list = [list(map(int, input().split())) for _ in range(M)]

ladders, snakes = dict(), dict()
for s, e in ladders_list:
    ladders[s] = e
for s, e in snakes_list:
    snakes[s] = e


# (pos, dice)
queue = deque([(1, 0)])
visited = [-1] * 101
visited[1] = 0

while queue:
    #print(queue)
    pos, dice = queue.popleft()

    #print(pos, dice)

    if pos == 100:
        print(dice)
        break

    for d in range(1, 7):
        next_pos = pos + d

        if next_pos > 100:
            break

        if visited[next_pos] == -1:
            # 방문처리는 사다리/뱀 도착한 곳이 아닌 시작한 곳 기준 기록
            visited[next_pos] = 0

            if next_pos in ladders:
                next_pos = ladders[next_pos]
            elif next_pos in snakes:
                next_pos = snakes[next_pos]
            
            queue.append((next_pos, dice+1))

