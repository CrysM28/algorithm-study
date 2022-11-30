# 12869. 뮤탈리스크
from collections import deque
from itertools import permutations

N = int(input())
scvs = list(map(int, input().split()))

if N < 3:
    for _ in range(3-N):
        scvs.append(0)



attack = 0
q = deque([scvs])
next_q = []
visited = set()

while q:
    scv = q.popleft()
    
    if scv[0] <= 0 and scv[1] <= 0 and scv[2] <= 0:
        break 

    for i in permutations([9,3,1]):
        a = scv[0] - i[0]
        b = scv[1] - i[1]
        c = scv[2] - i[2]

        a = 0 if a <= 0 else a
        b = 0 if b <= 0 else b
        c = 0 if c <= 0 else c

        if (a,b,c) not in visited:
            next_q.append([a, b, c])
            visited.add((a,b,c))
    
    if not q:
        attack += 1
        q = deque(next_q)
        next_q.clear()

print(attack)