# 2003. 수들의 합 2

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

start = 0
end = 0
tmp = arr[0]

while start < N:

    if tmp == M:
        answer += 1

        tmp -= arr[start]
        start += 1

        if end < N-1:
            end += 1
            tmp += arr[end]

    elif tmp < M:
        if end == N-1:
            tmp -= arr[start]
            start += 1
        else:
            end += 1
            tmp += arr[end]
    else:
        tmp -= arr[start]
        start += 1




print(answer)