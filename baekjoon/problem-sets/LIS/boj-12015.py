# 12015. 가장 긴 증가하는 부분 수열 2
import bisect

n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

for i in range(n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]

print(len(lis))
