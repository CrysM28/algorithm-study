# 15651. N과 M (3)

def backtrack(depth, arr):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        backtrack(depth+1, arr)
        arr.pop()



N, M = map(int, input().split())


backtrack(0, [])