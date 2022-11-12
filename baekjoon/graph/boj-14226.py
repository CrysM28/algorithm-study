# 14226. 이모티콘
from collections import deque

S = int(input())

time = 0
queue = deque([(1,0)])
next_q = []
visited = set()

while queue:
    screen, clipboard = queue.popleft()

    if screen == S:
        break
    
    if screen != 0 and (screen, screen) not in visited:
        next_q.append((screen, screen))
        visited.add((screen, screen))
    if clipboard != 0 and (screen+clipboard, clipboard) not in visited:
        next_q.append((screen+clipboard, clipboard))
        visited.add((screen+clipboard, clipboard))
    if screen - 1 >= 0 and (screen-1, clipboard) not in visited:
        next_q.append((screen-1, clipboard))
        visited.add((screen-1, clipboard))

    if not queue:
        queue = deque(next_q)
        next_q.clear()
        time += 1

print(time)