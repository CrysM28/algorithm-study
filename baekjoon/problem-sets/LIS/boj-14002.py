# 14002: 가장 긴 증가하는 부분 수열 4
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

# 기존 dp LIS와 동일 로직
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)


# 추가 로직: idx로 순서 찾기
idx = max(dp)
print(idx)

ans = deque([])
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        idx -= 1
        ans.appendleft(arr[i])
    if idx == 0:
        break

print(*ans)