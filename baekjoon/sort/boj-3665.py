# 3665. 최종 순위
from collections import defaultdict, deque

# 위상정렬
def ts(order):
    result = []
    q = deque()  # 우선순위 큐

    # 큐 초기화
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # 진입차수 재계산
        for i in range(1, n+1):
            if order[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        # q에 한 번에 하나만 들어와야 조건 충족
        if len(q) > 1:
            return result

    return result


for _ in range(int(input())):

    # 작년 순위
    n = int(input())    # 팀의 수
    indegree = [0 for _ in range(n+1)]     # 진입차수
    data = list(map(int, input().split()))
    rank = [[False] * (n+1) for _ in range(n+1)]   # 순위 그래프 (높 -> 낮)
    for i in range(n):
        for j in range(i+1, n):
            rank[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 바뀐 순위
    m = int(input())    # 등수 바뀐 팀의 수
    for i in range(m):
        a, b = map(int, input().split())    # a->b
        # 바뀌었으면 간선 뒤집기
        if rank[a][b]:
            rank[b][a] = True
            rank[a][b] = False
            indegree[b] -= 1
            indegree[a] += 1
        else:
            rank[a][b] = True
            rank[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1


    # 모든 원소 탐색하지 못했으면 순위 구할 수 없음
    result = ts(rank)
    if len(result) != n:
        print("IMPOSSIBLE")
    else:
        print(*result)