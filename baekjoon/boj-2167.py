
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())

    for a in range(i-1, x):
        for b in range(j-1, y):
            ans += arr[a][b]
    
    print(ans)

