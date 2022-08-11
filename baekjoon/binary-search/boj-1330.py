# 1330. K번째 수 -> "의외로 이분탐색으로 풀 수 있는 문제"

n = int(input())
k = int(input())
arr = sorted([a * b for a in range(1, n + 1) for b in range(1, n + 1)])

print(arr[k])