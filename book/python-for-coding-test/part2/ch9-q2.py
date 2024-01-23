# 미래 도시
## 가중치 없는 최단 경로는 BFS로도 가능

from collections import defaultdict, deque


def bfs(start, end):
    visited = [start]
    queue = deque([(start, 0)])    # (i, count)

    while queue:
        print(queue)
        v = queue.popleft()
        if v[0] == end:
            return v[1]

        for w in graph[v[0]]:
            if w not in visited:
                visited.append(w)
                queue.append((w, v[1]+1))

    # end에 도달하지 못하면
    return -1



# 회사 수, 경로 수
n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)    # 양방향

# 경로: 1 -> k -> x
x, k = map(int, input().split())


ans1 = bfs(1, k)
ans2 = bfs(k, x)

if ans1 == -1 or ans2 == -1:
    print(-1)
else:
    print(ans1 + ans2)

