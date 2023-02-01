# 9019. DSLR
from collections import deque

def dslr(n):
    d = (2*n) % 10000

    s = n-1
    if s == -1:
        s = 9999

    n_zero = str(n).zfill(4)
    l = int(n_zero[1:] + n_zero[0])
    r = int(n_zero[-1] + n_zero[:-1])

    return (d, s, l, r)


def add_queue(n, prev_n, ops):
    if path[n] == '':
        path[n] = [prev_n, ops]
        q.append(n)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    # [prev_path, operation]
    path = [''] * 10000
    path[a] = [a, 'X']

    q = deque([a])
    while q:
        num = q.popleft()

        if num == b:
            break

        d, s, l, r = dslr(num)

        add_queue(d, num, 'D')
        add_queue(s, num, 'S')
        add_queue(l, num, 'L')
        add_queue(r, num, 'R')

    
    prev_path, ops = path[b]
    ans = ""
    while ops != 'X':
        ans += ops
        prev_path, ops = path[prev_path]
    print(*ans[::-1], sep="")