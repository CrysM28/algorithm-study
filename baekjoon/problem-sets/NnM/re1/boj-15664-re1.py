# 15664. N과 M (10)

def backtrack():
    if len(visited) == M:
        results.append(visited[:])
        return

    remember = 0
    for i, n in enumerate(numbers):
        if not used[i] and remember != n:
            if not visited or n >= visited[-1]:
                remember = n
                used[i] = True
                visited.append(n)
                backtrack()
                used[i] = False
                visited.pop()



N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = []
results = []
used = [False] * N

backtrack()

for r in results:
    print(*r)