# 15666. N과 M (12)

def backtrack():
    if len(visited) == M:
        results.append(visited[:])
        return

    remember = 0
    for n in numbers:
        if remember != n:
            if not visited or n >= visited[-1]:
                remember = n
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