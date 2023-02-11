# 2623. 음악프로그램
from collections import deque, defaultdict

N, M = map(int, input().split())

# 입력 처리 (그래프, 진입차수)
graph = defaultdict(list)
indegree = [0] * (N+1)

for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(2, data[0]+1):
        graph[data[i-1]].append(data[i])
        indegree[data[i]] += 1

# 위상정렬
result = []

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)


if len(result) != N:
    print(0)
else:
    print(*result, sep='\n')
