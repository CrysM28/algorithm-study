# 5014. 스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())

can_go = False
count = 0

queue = deque([S])
next_q = []
visited = set([S])

while queue:
    now = queue.popleft()

    # 목표 층 도달
    if now == G:
        can_go = True
        break

    # 다음 층
    up = now + U
    down = now - D

    if up <= F and up not in visited:
        next_q.append(up)
        visited.add(up)
    
    if down >= 1 and down not in visited:
        next_q.append(down)
        visited.add(down)
    
    # 다음 레벨로
    if not queue:
        queue = deque(next_q)
        next_q.clear()
        count += 1


if can_go:
    print(count)
else:
    print("use the stairs")