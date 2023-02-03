# 15649. N과 M (1)

def backtrack():
    # 특정 깊이에 도달하면 그만
    if len(visited) == M:
        results.append(visited[:])
        return

    for i in range(1, N + 1):   # 1~N까지 다 보면서
        if i not in visited:    # 아직 보지 않은것만 (백트래킹)
            visited.append(i)
            backtrack()  # 재귀
            visited.pop()  # 답을 봤으면 되돌아가기


# 1~N 까지 중복없이 M개 고르기
N, M = map(int, input().split())

visited = []
results = []

backtrack()

for r in results:
    print(*r)