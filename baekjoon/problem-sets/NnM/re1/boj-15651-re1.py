# 15651. N과 M (3)

def backtrack():
    if len(visited) == M:
        results.append(visited[:])
        return

    for i in range(1, N+1):
        visited.append(i)
        backtrack()
        visited.pop()


N, M = map(int, input().split())

visited = []
results = []

backtrack()

for r in results:
    print(*r)