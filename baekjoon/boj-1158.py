# 1158. 요세푸스 문제
from collections import deque

N, K = map(int, input().split())
ans = []

q = deque([i for i in range(1, N+1)])

cnt = K
while q:
    v = q.popleft()
    if cnt == 1:
        ans.append(v)
        cnt = K
    else:
        cnt -= 1
        q.append(v)


print('<' + ', '.join(list(map(str, ans))) + '>')