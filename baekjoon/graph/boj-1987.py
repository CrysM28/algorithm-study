# 1987. 알파벳
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

queue = set([(0, 0, arr[0][0])])
answer = 0
while queue:
    #print(queue)
    i, j, visited = queue.pop()
    answer = max(answer, len(visited))

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] not in visited:
            queue.add((ni, nj, visited + arr[ni][nj]))

print(answer)