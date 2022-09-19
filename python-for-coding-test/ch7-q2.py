# 부품 찾기

def bs(target):
    start, end = 0, len(store) - 1

    while start <= end:
        mid = (start + end) // 2
        if store[mid] > target:
            end = mid - 1
        elif store[mid] < target:
            start = mid + 1
        else:
            return mid

    # 못 찾음
    return -1


# 가게에 있는 부품
n = int(input())
store = sorted(list(map(int, input().split())))

# 손님 확인 요청
m = int(input())
customer = list(map(int, input().split()))

for c in customer:
    ans = bs(c)
    if ans == -1:
        print("no", end=" ")
    else:
        print("yes", end=" ")
