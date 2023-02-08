# 14002: 가장 긴 증가하는 부분 수열 5
import bisect
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

lis_len = [arr[0]]
lis_idx = [1] * n

for i in range(n):
    if arr[i] > lis_len[-1]:
        lis_len.append(arr[i])
        lis_idx[i] = len(lis_len)
    else:
        idx = bisect.bisect_left(lis_len, arr[i])
        lis_len[idx] = arr[i]
        lis_idx[i] = idx+1

idx = len(lis_len)
print(idx)

ans = deque([])
for i in range(n-1, -1, -1):
    if lis_idx[i] == idx:
        idx -= 1
        ans.appendleft(arr[i])
    if idx == 0:
        break

print(*ans)
