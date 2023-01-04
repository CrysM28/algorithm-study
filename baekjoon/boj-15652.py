# 15652. N과 M (4)
def backtrack(arr, depth):
    if depth == M:
        result.append(arr[::])
        return

    for i in range(1, N+1):
        if not arr or i >= arr[-1]:
            arr.append(i)
            backtrack(arr, depth+1)
            arr.pop()


N, M = map(int, input().split())
result = []

backtrack([], 0)

for r in result:
    print(*r)