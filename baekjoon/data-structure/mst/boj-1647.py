# 1647. 도시 분할 계획

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if a < b:
        p[b] = a
    else:
        p[a] = b
    return True


n, m = map(int, input().split())
p = [i for i in range(n + 1)]

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

total = []
for c, a, b in edges:
    if union(a, b):
        total.append(c)

answer = sum(total[:-1])
print(answer)
