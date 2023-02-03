# 20040. 사이클 게임

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    # 같은 집합이면 사이클 발생
    if a == b:
        return True

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False


n, m = map(int, input().split())

parent = [i for i in range(n)]
edges = [list(map(int, input().split())) for _ in range(m)]


for i, edge in enumerate(edges):
    a, b = edge

    if union(a, b):
        print(i+1)
        break
else:
    print(0)

