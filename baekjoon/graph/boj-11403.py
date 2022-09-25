# 11403. 경로 찾기
from collections import deque

def bfs(start_v):
    visited = []    # 다시 돌아오는 경우에만 추가해줘야 해서 뺌
    queue = deque([start_v])

    while queue:
        v = queue.popleft()

        for i in range(N):
            if adj[v][i] == 1 and i not in visited:
                 visited.append(i)
                 queue.append(i)                

    return visited

# 입력
N = int(input())
adj = []
path = [[0] * N for _ in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    adj += tmp,

# 방문 시에만 경로 있음
for i in range(N):
    visit = set(bfs(i))
    for j in range(N):
        if j in visit:
            path[i][j] = 1

# 출력
for p in path:
    print(*p)