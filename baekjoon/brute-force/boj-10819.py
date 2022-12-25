# 10819. 차이를 최대로

N = int(input())
numbers = list(map(int, input().split()))

max_val = 0
visited = [0] * N


def get_result(arr):
    global max_val
    result = 0
    for i in range(N-1):
        result += abs(arr[i] - arr[i+1])
    max_val = max(max_val, result)


def get_all_perms(arr, cnt):
    if cnt == N:
        get_result(arr)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(numbers[i])
            get_all_perms(arr, cnt+1)
            arr.pop()
            visited[i] = 0


get_all_perms([], 0)
print(max_val)