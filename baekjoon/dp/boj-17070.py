# 17070. 파이프 옮기기 1
## 참고: https://aia1235.tistory.com/17

# 표기
EMPTY = 0
WALL = 1

# 방향
HOR = 0     # 가로
VER = 1     # 세로
DIAG = 2    # 대각


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

# dp[방향][x][y] == (x,y) 좌표에 (방향)으로 놓일 수 있는 경우의 수
dp = [[[0]*N for _ in range(N)] for _ in range(3)]

# 초기화: 가로 방향
dp[HOR][0][1] = 1
for i in range(2, N):
    if home[0][i] == EMPTY:
        dp[HOR][0][i] = 1
    else:
        break

# 나머지 체크
for i in range(1, N):
    for j in range(1, N):
        if home[i][j] == EMPTY:
            # 가로 놓기
            dp[HOR][i][j] = dp[HOR][i][j-1] + dp[DIAG][i][j-1]
            # 세로 놓기
            dp[VER][i][j] = dp[VER][i-1][j] + dp[DIAG][i-1][j]

        # 대각 놓기
        if home[i][j] + home[i][j-1] + home[i-1][j] == EMPTY:
            dp[DIAG][i][j] = dp[HOR][i-1][j-1] + dp[VER][i-1][j-1] + dp[DIAG][i-1][j-1]

ans = 0
for i in range(3):
    ans += dp[i][N-1][N-1]
print(ans)