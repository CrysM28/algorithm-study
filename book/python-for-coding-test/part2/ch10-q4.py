# 커리큘럼
from collections import defaultdict, deque
import copy

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 수행 결과
    q = deque()  # 큐

    # 진입차수 0인 노드들을 큐에 넣고 시작
    for i in range(1, n + 1):
        if i not in indegree:
            q.append(i)

    while q:
        now = q.popleft()

        for i in course[now]:
            result[i] = max(result[i], result[now] + time[i])

            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result


# 강의 수
n = int(input())
course = defaultdict(list)
time = defaultdict(int)
indegree = defaultdict(int)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 강의에 걸리는 시간
    for d in data[1:-1]:  # 선수과목
        course[d].append(i)
        indegree[i] += 1


ans = topology_sort()
print(*ans.values(), sep="\n")

