# 2775. 부녀회장이 될테야

apart = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if j == 0:
            continue
        if i == 0:
            apart[i][j] = j
            continue
        
        apart[i][j] = apart[i-1][j] + apart[i][j-1]


for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(apart[k][n])
