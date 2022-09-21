# 2252. 줄 세우기

from collections import deque, defaultdict

# 위상 정렬 함수
def topology_sort():
    result = [] 
    q = deque() 

    for i in range(1, v + 1):
        if i not in indegree:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
  
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result


# 정점, 간선 수
v, e = map(int, input().split())
# 진입차수
indegree = defaultdict(int)

graph = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())