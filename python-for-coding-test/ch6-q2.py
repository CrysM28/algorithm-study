# 위에서 아래로

n = int(input())
arr = [int(input()) for _ in range(n)]

print(*sorted(arr, reverse = True))