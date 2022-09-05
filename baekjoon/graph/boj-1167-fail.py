# 1167. 트리의 지름
## 시간초과
from collections import defaultdict

cur_max = 0

def dfs(v, l):
    global cur_max
    #cur_sum = l
    print("in v", v, "cur_sum", l)
    visited.append(v)
    print("visit", visited)
    for w in graph[v]:
        if w[0] not in visited:
            print(visited, w)
            cur_sum = dfs(w[0], l+w[1])
            print(cur_sum, l)
            cur_max = max(cur_sum, cur_max)
            #cur_max = max(cur_sum, cur_max)

    #print("v", v,"is returning", cur_sum)
    return l


# 트리의 정점의 개수
V = int(input())

# 간선 정보 저장
graph = defaultdict(list)
for _ in range(V):
    inputs = list(map(int, input().split()))
    a = inputs[0]

    for i in range(1, len(inputs), 2):
        if inputs[i] == -1:
            break
        b, cost = inputs[i], inputs[i + 1]
        graph[a].append((b, cost))

# 지름 (최대 거리)
diameter = 0

# 각 노드에 대해 dfs 수행 후 최대 길이 저장
for i in range(1, V + 1):
    visited = []
    cur_max = 0
    dfs(i, 0)
    diameter = max(diameter, cur_max)

print(diameter)