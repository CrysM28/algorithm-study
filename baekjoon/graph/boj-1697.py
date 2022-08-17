# 1697. 숨바꼭질
## BFS
## PyPy3 - 236 ms, Python3 - 360 ms

from collections import deque

N, K = map(int, input().split())

checked = set([N])  # 이미 체크한 수는 패스할 수 있게 -> in 효율을 위한 set
q1 = deque([N])     # BFS queue - 같은 level에 있는 노드 -> popleft 효율을 위한 deque
q2 = []             # BFS queue - 다음 level 노드
t = 0               # 걸린 시간 (초)

while True:
    # 현 레벨의 모든 노드 체크 완료 -> 다음 레벨로 넘어가면서 초 +1
    if not q1:
        q1 = deque(q2[:]) 
        q2 = [] 
        t += 1  
        continue

    # 현 레벨의 노드 차례대로 체크
    cur = q1.popleft()

    # 찾음
    if cur == K:
        print(t)
        break

    # 이동 가능한 다음 숫자 - 백트래킹 
    next = [cur + 1, cur - 1]
    if cur < K:
        next.append(cur * 2)
    ## cur >= K면 cur*2에서 K까지 빼는것보다 K번 더하는 게 빠르므로 제외

    # 체크한 적 없는 숫자에 대해서만 작업
    for n in next:
        if n not in checked:
            q2.append(n)
            checked.add(n)
