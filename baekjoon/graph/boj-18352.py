# 18352. 특정 거리의 도시 찾기
from collections import defaultdict, deque

def bfs(start, min_dist):
    visited = {start}
    queue = deque([[start, 0]])
    dist_city = []

    while queue:
        v, dist = queue.popleft()

        # 같은 거리인 도시만 저장
        if dist == min_dist:
            dist_city.append(v)
            continue

        # 종료 조건
        elif dist > min_dist:
            return dist_city

        # 아직 아닐 때 주변 노드 더하기
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                queue.append([w, dist+1])


    return dist_city

# v, e, 최단 거리, 출발도시번호
n,m,k,x = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


result = bfs(x, k)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(*result, sep="\n")
