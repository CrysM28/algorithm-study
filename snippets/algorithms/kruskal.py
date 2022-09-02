from collections import defaultdict

# 입력: 정점, 간선 개수
V, E = map(int, input().split())

# 부모를 자기 자신으로 초기화
parent = defaultdict(int)
for i in range(1, V + 1):
    parent[i] = i


# Find: x의 root 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression 적용
    return parent[x]


# Union: 두 집합을 병합
def union(a, b):
    # 각각의 root 노드 찾기
    a = find(a)
    b = find(b)

    # 같은 집합이면 사이클 발생
    if a == b:
        return True

    # 다른 집합이면 더 작은 쪽을 부모로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False

# union-find.py
#####################################################

# 입력: 간선 정보
edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()    # 간선 비용 기준 오름차순 정렬


total_cost = 0
for edge in edges:
    cost, a, b = edge
    # # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    # if find(parent, a) != find(parent, b):
    #     union(parent, a, b)

    # 사이클 발생하지 않으면 MST에 포함
    if not union(parent, a, b):
        total_cost += cost

print(total_cost)

