# 15655. N과 M (6)

def backtrack():
    if len(visited) == M:
        results.append(visited[:])
        return

    for n in numbers:
        if not visited or n > visited[-1]:
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