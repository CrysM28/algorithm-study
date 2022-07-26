from collections import deque, defaultdict

# 위상 정렬 함수
def topology_sort():
    result = []  # 수행 결과
    q = deque()  # 큐

    # 진입차수 0인 노드들을 큐에 넣고 시작
    for i in range(1, v + 1):
        if i not in indegree:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            # 연결된 노드들의 진입차수-1
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    return result


# 정점, 간선 수
v, e = map(int, input().split())

# 진입차수
indegree = defaultdict(int)

# 간선 입력
graph = defaultdict(list)
for _ in range(e):
    # a -> b 순서
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(topology_sort())