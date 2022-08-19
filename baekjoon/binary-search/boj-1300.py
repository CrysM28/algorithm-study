# 1300. K번째 수

n = int(input())
k = int(input())
arr = sorted([a * b for a in range(1, n + 1) for b in range(1, n + 1)])

print(arr[k])