# 15656. N과 M (7)

def backtrack():
    if len(visited) == M:
        results.append(visited[:])
        return

    for n in numbers:
        visited.append(n)
        backtrack()
        visited.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = []
results = []

backtrack()

for r in results:
    print(*r)