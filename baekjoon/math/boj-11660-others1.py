#Book - 어디 책에 나오는 문제인가 봄

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# 인덱싱 편리함을 위해 원본 리스트에도 index 0 부분에 padding 0
A = [[0] * (n + 1)]
# 합 배열 공식에 따라 합을 구하기 위한 padding 넣어주기 : index 0 부분에 0으로!
D = [[0] * (n + 1) for _ in range(n + 1)]

#A 배열 index : [0~n][0~n] : N+1개 rows&colums
for i in range(n):
    #원본 리스트 추가에도 index 0 부분에 0 추가해서 append
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

#D 합 배열
for i in range(1, n + 1):  #index 1부터 시작 주의
    for j in range(1, n + 1):  #index 1부터 시작 주의
        D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + A[i][j]

#result 구간 합
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
