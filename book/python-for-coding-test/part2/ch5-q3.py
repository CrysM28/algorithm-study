# 음료수 얼려 먹기

def dfs(i, j):
    # 종료 조건
    if i < 0 or i >= n or j < 0 or j >= m or arr[i][j] != 0:
        return

    # 방문 표시
    arr[i][j] = 2

    # 상하좌우
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)



# 입력
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr += list(map(int, input())),

# 묶음 세기
cnt = 0
for ii in range(n):
    for jj in range(m):
        if arr[ii][jj] == 0:
            dfs(ii, jj)
            cnt += 1

print(cnt)
