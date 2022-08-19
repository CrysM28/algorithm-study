# 11724. 연결 요소의 개수

# 정점, 간선
N, M = map(int, input().split())
nodes = [x for x in range(1, N+1)]

# 인접 리스트 저장
arr = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

# DFS로 탐색 -> 스택 구현
cnt = 0

# 모든 노드 리스트에서 방문한 노드는 삭제해서 빌 때까지 반복
while nodes:   
    stack = [nodes[0]]
    while stack:
        v = stack.pop()
        if v in nodes:
            nodes.remove(v)         
            for w in arr[v]:
                stack.append(w)
    cnt += 1

print(cnt)