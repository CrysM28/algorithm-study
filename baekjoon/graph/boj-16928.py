# 16928. 뱀과 사다리 게임
### BFS로 푸는 거랑 우선순위 큐로 푸는거나 q 뽑는 방식만 다르고 동작은 동일

from collections import defaultdict, deque
import heapq as h

# 사다리 n, 뱀 m
n, m = map(int, input().split())

# 사다리. 뱀 : {출발지점: 도착지점}
ladders = defaultdict(int)
snakes = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b


# 방문한 지점 표시 -> 주사위로 도착한 곳만
visited = defaultdict(bool)
# (위치, 굴린 주사위 수)
q = [[0, 1]]
#q = deque([[1, 0]])

while q:
    dice, pos = h.heappop(q)
    #pos, dice = q.popleft()

    # 도착지점 도착시 
    if pos == 100:
        break
    # 넘어가면 취급 안함
    elif pos > 100:
        continue

    # 주사위 굴리기
    rolled = False
    for i in range(6, 0, -1):
        next_pos = pos + i

        # 주사위 굴려서 방문했던 곳이면 패스
        if visited[next_pos]:
            continue

        # 중간에 사다리나 뱀 있으면 일단 타보기
        if next_pos in ladders:
            visited[next_pos] = True
            h.heappush(q,[dice + 1, ladders[next_pos]])
        elif next_pos in snakes:
            visited[next_pos] = True
            h.heappush(q, [dice + 1, snakes[next_pos]])
        
        # 그냥 굴리기 -> 최대값 한 번만 저장
        else:
            if not rolled and next_pos <= 100:
                rolled = True
                visited[next_pos] = True
                h.heappush(q,[dice + 1,next_pos])


print(dice)