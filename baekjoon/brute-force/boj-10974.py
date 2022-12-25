# 10974. 모든 순열


N = int(input())
visited = [0] * (N+1)
answer = []

def make_permutation(arr, cnt):
    if cnt == N:
        answer.append(arr[::])
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            make_permutation(arr, cnt+1)
            arr.pop()
            visited[i] = 0


make_permutation([], 0)

for a in answer:
    print(*a)
