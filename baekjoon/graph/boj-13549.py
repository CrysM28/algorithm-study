# 13549. 숨바꼭질 3
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([n])
next_q = []
visited = set()
time = 0
end = False

while not end:
    print(q)
    while q:
        # 현 위치 확인
        pos = q.popleft()
        if pos == k:
            end = True
            break
        visited.add(pos)

        # 0초 후 (*2)
        pos2 = pos * 2
        if pos2 != 0:
            while pos2 < k*2:
                if pos2 not in visited:
                    q.append(pos2)
                    visited.add(pos2)
                pos2 *= 2

        # 1초 후 (+-1)
        for next_pos in [pos + 1, pos - 1]:
            if next_pos in visited or next_pos < 0:
                continue
            next_q.append(next_pos)
            visited.add(next_pos)

    # 못 찾았으면 1초 후 확인
    if not end:
        q = deque(next_q)
        next_q.clear()
        time += 1


print(time)