dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        # 조건 맞을 때만 재귀하게 해서 시간 아끼기 (좋은 듯?)
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)      # 굳이 defaultdict 할필요 없이 append로

print(len(result))
for i in sorted(result):
    print(i)