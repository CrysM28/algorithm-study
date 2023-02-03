# 15657. N과 M (8)

def backtrack(arr, depth):
    if depth == M:
        print(*arr)
        return
    
    for n in nums:
        if arr and n < arr[-1]:
            continue
        arr.append(n)
        backtrack(arr, depth+1)
        arr.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

backtrack([], 0)