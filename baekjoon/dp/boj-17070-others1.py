N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))
pipe = []
for _ in range(N):
    pipe.append([[0, 0, 0] for _ in range(N)])
pipe[0][1][0] = 1
home[0][1] = 1

for i in range(N):
    for j in range(1, N):
        if home[i][j] == 1:
            continue
        if j != 0:
            pipe[i][j][0] = pipe[i][j-1][0] + pipe[i][j-1][1]
        if i != 0:
            pipe[i][j][2] = pipe[i-1][j][1] + pipe[i-1][j][2]
        if i != 0 and j != 0 and home[i-1][j] != 1 and home[i][j-1] != 1:
            pipe[i][j][1] = sum(pipe[i-1][j-1])
print(sum(pipe[N-1][N-1]))