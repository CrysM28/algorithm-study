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
