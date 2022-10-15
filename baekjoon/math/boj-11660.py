# 11660. 구간 합 구하기 5
import sys
input = sys.stdin.readline

# 누적합 배열
def get_sum_array(arr):
    row = len(arr)
    col = len(arr[0])

    # 행의 합
    sum_array = [[sum(arr[i][:j + 1]) for j in range(col)] for i in range(row)]
    # 열의 합
    for i in range(row - 1):
        for j in range(col):
            sum_array[i + 1][j] += sum_array[i][j]

    return sum_array


# (x1, y1) ~ (x2, y2)의 구간합
def prefix_sum_2d(S, x1, y1, x2, y2):
    sum1 = S[x2][y2]
    sum2 = S[x1 - 1][y2]
    sum3 = S[x2][y1 - 1]
    sum4 = S[x1 - 1][y1 - 1]

    if x1 == 0:
        sum2 = 0
        sum4 = 0
    if y1 == 0:
        sum3 = 0
        sum4 = 0

    # print(x1, y1, x2, y2)
    # print(sum1, sum2, sum3, sum4)
    return sum1 - (sum2 + sum3) + sum4


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 누적합 배열 구해놓기
S = get_sum_array(arr)
# print(*S, sep='\n')

# (x1,y1) ~ (x2,y2) 합 구하기
for _ in range(m):
    pos = list(map(int, input().split()))

    answer = prefix_sum_2d(S, pos[0]-1, pos[1]-1, pos[2]-1, pos[3]-1)
    print(answer)
