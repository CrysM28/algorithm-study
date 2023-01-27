# 11660. 구간 합 구하기 5

import sys
input = sys.stdin.readline

# 누적합 배열 구하기
def get_sum_array(sum_arr, row, col):
    sum_arr = [[0] * (row+1) for _ in range(col+1)]

    for i in range(1, row+1):
        for j in range(1, col+1):
            sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1] + arr[i][j]

    return sum_arr

# (x1, y1) ~ (x2, y2)의 구간합
def prefix_sum_2d(S, x1, y1, x2, y2):
    sum1 = S[x2][y2]
    sum2 = S[x1-1][y2]
    sum3 = S[x2][y1-1]
    sum4 = S[x1-1][y1-1]

    return sum1 - (sum2 + sum3) + sum4


n, m = map(int, input().split())
arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0]+ list(map(int, input().split())))

S = get_sum_array(arr, n, n)

for _ in range(m):
    pos = list(map(int, input().split()))
    answer = prefix_sum_2d(S, pos[0], pos[1], pos[2], pos[3])
    print(answer)
