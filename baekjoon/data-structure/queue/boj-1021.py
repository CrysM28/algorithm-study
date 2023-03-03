# 1021. 회전하는 큐
from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

cnt = 0

for p in pos:
    while True:
        if q[0] == p:
            q.popleft()
            break

        # 왼쪽 회전
        if q.index(p) < len(q) / 2:
            while q[0] != p:
                q.append(q.popleft())
                cnt += 1
        
        # 오른쪽 회전
        else:
            while q[0] != p:
                q.appendleft(q.pop())
                cnt += 1

print(cnt)