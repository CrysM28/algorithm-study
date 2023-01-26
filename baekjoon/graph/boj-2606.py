# 2606. 바이러스

## 그래프 탐색하면서 수 세면 되는 문제
## bfs, dfs는 상관 없을 거 같지만 속도가 조금이라도 빠른 bfs로 구현해보자
### 이 풀이는 DFS 입니다... deque를 썼다고 BFS인 것은 아니거든요...

from collections import deque

# 컴퓨터 개수(node)만큼 인접리스트 생성
connected = [[] for _ in range(int(input()) + 1)]
for i in range(int(input())):
    start, end = map(int, input().split())
    connected[start].append(end)
    connected[end].append(start)

# queue가 빌때까지 BFS
visited = []
queue = deque([1])

while queue:
    q = queue.popleft()
    if q not in visited:
        visited.append(q)
        for c in connected[q]:
            queue.append(c)

# 시작한 1번 컴퓨터를 제외한 감염 수
print(len(visited) - 1)
