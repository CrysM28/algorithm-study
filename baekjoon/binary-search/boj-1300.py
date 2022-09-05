# 1300. K번째 수
## B[k] = x : x보다 작거나 같은 원소의 수가 최소 K개


def decision(x):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(x // i, n)
    return cnt


n = int(input())  # 배열 크기
k = int(input())  # 인덱스

# B[k]가 될 x의 범위
start, end = 1, k

# x에 대해 매개변수 탐색
while start <= end:
    mid = (start + end) // 2

    # x보다 작거나 같은 원소의 수
    x_num = decision(mid)

    ## lower-bound (찾고자 하는 값과 같거나 큰 수의 첫번째 인덱스)
    # x를 줄여서 x_sum을 줄이기
    if x_num >= k:
        end = mid - 1

    # x를 늘려서 x_sum을 늘리기
    elif x_num < k:
        start = mid + 1

print(start)