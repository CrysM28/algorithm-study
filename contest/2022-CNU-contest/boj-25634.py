# 25634. 전구 상태 뒤집기
# defaultdict와 max(values) 사용

from collections import defaultdict

N = int(input())
brightness = list(map(int, input().split()))
power = list(map(int, input().split()))
dp = defaultdict(int)

max_brightness = 0
dp[-1] = -int(1e9)

for i in range(N):
    val = brightness[i]
    if power[i] == 1:
        val *= -1
        max_brightness += brightness[i]
    dp[i] = max(dp[i-1]+val, val)

print(max_brightness + max(dp.values()))
