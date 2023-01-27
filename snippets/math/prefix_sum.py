# 누적합
## s[x~y] = s[y] - s[x-1]

## 1차원 
n = int(input())
a = [0] + list(map(int, input().split())) 
s = [0] * (n + 1)

# 누적합 배열 만들기
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

# 구간합 구하기
x, y = map(int, input().split())
prefix_sum = s[y] - s[x-1]


## 2차원
row, col = map(int, input().split())

# 구현 편의를 위한 0 패딩
arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0]+ list(map(int, input().split())))


# 누적합 배열 만들기
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

