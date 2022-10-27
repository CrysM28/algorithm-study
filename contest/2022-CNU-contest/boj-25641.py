# 25641. 균형 잡힌 소떡소떡
from collections import deque

n = int(input())
stst = deque(input())

# 개수 세기
s, t = 0, 0
for st in stst:
    if st == 's':
        s += 1
    else:
        t += 1


while t != s:
    st = stst.popleft()
    if st == 's':
        s -= 1
    else:
        t -= 1


print(''.join(stst))
