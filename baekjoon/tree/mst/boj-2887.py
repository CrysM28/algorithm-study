# 2887. 행성 터널


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

# 행성 좌표: x,y,z 따로 관리
x, y, z = [], [], []
for i in range(n):
    planet = (list(map(int, input().split())))
    # (좌표, 번호)
    x.append((planet[0], i))
    y.append((planet[1], i))
    z.append((planet[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort() 

# 크루스칼
total_cost = 0
for cost, a, b in edges:
    if union(a, b):
        total_cost += cost

print(total_cost)
