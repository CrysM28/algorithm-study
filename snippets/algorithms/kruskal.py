# 입력: 정점, 간선 개수
V, E = map(int, input().split())

# 부모를 자기 자신으로 초기화
parent = [i for i in range(V + 1)]


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

# 크루스칼
for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않으면 MST에 포함
    if not union(a, b):
        total_cost += cost

print(total_cost)
