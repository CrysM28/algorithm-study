# 3665. 최종 순위
from collections import defaultdict
import heapq as h

# 위상정렬
def ts():
    result = []
    q = []  # 우선순위 큐

    # 큐 초기화
    for i in range(1, n+1):
        if i not in indegree:
            h.heappush(q, i)

    while q:
        now = h.heappop(q)
        result.append(now)

        # 차수 관리
        for i in order[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                h.heappush(q, i)

    return result


# 문제 수, 선수 수
n, m = map(int, input().split())

order = defaultdict(list)
indegree = defaultdict(int)

for i in range(m):
    a, b = map(int, input().split())
    order[a].append(b)
    indegree[b] += 1

print(*ts())