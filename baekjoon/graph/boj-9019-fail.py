# 9019. DSLR
## set check 없었을 땐 메모리초과
## 해결하니 시간초과

from collections import deque


# 연산
def DSLR(x):
    # D
    d = str((int(x) * 2) % 10000)
    if len(d) < 4:
        tmp = '0' * (4 - len(d))
        d = tmp + d

    # S
    if x == '0000':
        s = '9999'
    else:
        s = str(int(x) - 1)
        if len(s) < 4:
            tmp = '0' * (4 - len(s))
            s = tmp + s

    # L
    l = x[1:] + x[0]
    # R
    r = x[-1] + x[:-1]

    return (d, s, l, r)


# BFS로 하나씩 검사
def bfs(a, b):
    q = deque([[a, '']])
    checked = set()


    while q:
        now = q.popleft()

        # b와 같으면 종료
        if now[0] == b:
            return now

        # 연산 수행
        d, s, l, r = DSLR(now[0])

        # 연산 줄이기 -> 확인한 적 있으면 다시 확인 X
        if d not in checked:
            checked.add(d)
            q.append([d, now[1]+'D'])
        if s not in checked:
            checked.add(s)
            q.append([s, now[1]+'S'])
        if l not in checked:
            checked.add(l)
            q.append([l, now[1]+'L'])
        if r not in checked:
            checked.add(r)
            q.append([r, now[1]+'R'])
        
        

T = int(input())
for _ in range(T):
    # input
    A, B = input().split()
    if len(A) < 4:
        tmp = '0' * (4 - len(A))
        A = tmp + A
    if len(B) < 4:
        tmp = '0' * (4 - len(B))
        B = tmp + B

    
    ans = bfs(A, B)
    print(ans[1])
