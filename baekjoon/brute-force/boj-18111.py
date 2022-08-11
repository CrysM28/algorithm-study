# 18111. 마인크래프트
from collections import Counter

n, m, b = map(int, input().split())
grounds = []
for _ in range(n):
    grounds += list(map(int, input().split()))

min_time = 1e9
max_ground = 0

# 모든 땅의 높이에 대해 확인
for g_height in range(0, 257):
    time = 0
    blocks = b

    for g in grounds:
        # 깎기
        if g > g_height:
            time += (g - g_height) * 2
            blocks += g - g_height
        # 쌓기
        elif g < g_height:
            time += g_height - g
            blocks -= g_height - g
    if blocks < 0: continue  # 블럭 개수 모자라면 X

    min_time = min(time, min_time)
    if min_time == time:
        max_ground = g_height  # 같은 시간이면 더 높은 땅으로 갱신됨

print(min_time, max_ground)