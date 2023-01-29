# 15663. N과 M (9)

def backtrack(n, arr):
    if n == M:
        if tuple(arr) not in answers:
            answers.add(tuple(arr))
            print(*arr)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(nums[i])
            backtrack(n+1, arr)
            visited[i] = 0
            arr.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N
answers = set()

backtrack(0, [])
