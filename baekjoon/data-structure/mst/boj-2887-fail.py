# 2887. 행성 터널
## 메모리 초과, 시간 초과
## 모든 간선을 고려하는 방식으로는 안 됨

# union-find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True



n = int(input())
parent = [i for i in range(n + 1)]

planet = []
for _ in range(n):
    planet.append(list(map(int, input().split())))

# 간선 생성
edges = []
for i in range(n):
    for j in range(n):
        if i <= j:
            continue
        else:
            cost = min(abs(planet[i][0] - planet[j][0]),
                       abs(planet[i][1] - planet[j][1]),
                       abs(planet[i][2] - planet[j][2]))
        edges.append((cost, i, j))


edges.sort()    # 간선 비용 기준 오름차순 정렬


# 크루스칼
total_cost = 0
for cost, a, b in edges:
    if union(a, b):
        total_cost += cost

print(total_cost)
