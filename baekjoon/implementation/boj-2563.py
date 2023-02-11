# 2563. 색종이

paper = [[0] * 100 for _ in range(100)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)