# 15654. N과 M (5)

# 중복없이 M개 고르기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def backtrack():
    # 특정 깊이에 도달하면 그만
    if len(visited) == M:
        results.append(visited[:])
        return

    for num in numbers:
        if num not in visited:    # 아직 보지 않은것만 확인
            visited.append(num)
            backtrack()     # 재귀
            visited.pop()   # 백트래킹


visited = []
results = []

backtrack()

for result in results:
    print(*result)