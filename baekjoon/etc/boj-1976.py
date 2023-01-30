# 1976. 여행 가자

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:   parent[b] = a
    else:   parent[a] = b


N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

for i in range(1, N+1):
    cities = list(map(int, input().split()))
    for j in range(1, N+1):
        if cities[j-1] == 1:
            union(i, j)

travel = set(map(int, input().split()))

prev = 0
connected = True
for t in travel:
    if prev == 0:
        prev = find(t)
        continue
    
    cur = find(t)
    if prev != cur:
        connected = False
        break

if connected:
    print("YES")
else:
    print("NO")

