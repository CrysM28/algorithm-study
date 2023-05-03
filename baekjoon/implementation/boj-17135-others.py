from copy import deepcopy
from collections import deque

N, M, D = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
dr = [(0, -1), (-1, 0), (1, 0), (0, 1)]
a = [0] * M
m = 0


def DFS(u, n):
    if not n:
        game()
        return
    for v in range(u + 1, M):
        a[v] = 1
        DFS(v, n - 1)
        a[v] = 0


def BFS(B, n):
    V = [[-1] * M for _ in range(N + 1)]
    V[N][n] = 0
    q = deque([(N, n)])
    while q:
        x, y = q.popleft()
        if V[x][y] < D:
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                if 0 <= tx < N and 0 <= ty < M and V[tx][ty] == -1:
                    if B[tx][ty]: return tx, ty
                    else:
                        V[tx][ty] = V[x][y] + 1
                        q.append((tx, ty))
                elif tx == N and 0 <= ty < M and V[tx][ty] == -1:
                    V[tx][ty] = V[x][y] + 1
                    q.append((tx, ty))
    return -1, -1


def game():
    global m
    b, c = deepcopy(A), 0
    for _ in range(N):
        for x, y in remove_enemy(b):
            b[x][y] = 0
            c += 1
        b = move(b)
    m = max(m, c)


def move(B):
    C = [[0] * M]
    for i in range(N - 1):
        C.append(B[i])
    return C


def remove_enemy(B):
    e = []
    for i, ar in enumerate(a):
        if ar:
            x, y = BFS(B, i)
            if x != -1 and (x, y) not in e:
                e.append((x, y))
    return e


for i in range(M - 2):
    a[i] = 1
    DFS(i, 2)
    a[i] = 0
print(m)