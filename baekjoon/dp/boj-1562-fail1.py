# 1562. 계단 수
# 2개 둬도 되지만 3차원 배열로 처리하는 게 로직상 깔끔할듯
DIV = int(1e9)
n = int(input())

# 계단수 개수
dp1 = [[0]* 10 for _ in range(n+1)]
# 계단수 나타난 숫자 (bitmask)
dp2 = [[0]* 10 for _ in range(n+1)]

# 기본값
for i in range(10):
    dp1[1][i] = 1
    dp2[1][i] = 1 << i
dp1[1][0] = 0

cnt = 0

# bottom-up DP
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp1[i][j] = dp1[i-1][1]
            dp2[i][j] = dp2[i-1][1] | (1<<j)
        elif j == 9:
            dp1[i][j] = dp1[i-1][8]
            dp2[i][j] = dp2[i-1][8] | (1<<j)
        else:
            dp1[i][j] = dp1[i-1][j-1] + dp1[i-1][j+1]
            dp2[i][j] = dp2[i-1][j-1] | dp2[i-1][j+1] | (1<<j)
            print("==", i, j)
            print('{:#b}'.format(dp2[i][j]))

        if dp2[i][j] == (1<<10) - 1:
            print(i, j, dp1[i][j])
            cnt += dp1[i][j]

    #print("==", i)
    #print(*dp2, sep='\n')

print(cnt%DIV)

#print('{:#b}'.format(1<<10))
#print(*dp2, sep='\n')