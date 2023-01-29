# 12851. 숨바꼭질 2
## 처음 방법이 조금 더 빠름
## (꺼낼 때가 아닌 마지막에 넣을 때 갱신 한번에 처리) 

from collections import deque

MAX = 100001
N, K = map(int, input().split())

cnt = 0
time = 0

queue = deque([N])
prev_q, next_q = [N], []

visited = set()
tmp = []

while queue:
    x = queue.popleft()

    # 꺼낼 때 갱신
    visited.add(x)

    # 같은 레벨 내 최단거리 개수 찾기
    if x == K:
        for q in prev_q:
            if q == K: cnt += 1
        break
    
    # 다음 레벨 큐 넣기 (같은 레벨 안에는 중복이 있을 수 있도록 visited 갱신 X)
    for next in (x+1, x-1, x*2):
        if 0 <= next < MAX and next not in visited:
            next_q.append(next)
            #tmp.append(next)
    
    if not queue:
        print(next_q)
        time += 1

        # visited 갱신을 한 박자 늦게
        #visited.update(tmp)
        #tmp.clear()

        # 다음 레벨
        queue = deque(next_q)
        prev_q = next_q[::]
        next_q.clear()
        
print(time)
print(cnt)
