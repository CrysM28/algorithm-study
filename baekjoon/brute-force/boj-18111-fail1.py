# 18111. 마인크래프트
from collections import Counter

n, m, b = map(int, input().split())
grounds = []
for _ in range(n):
    grounds += list(map(int, input().split()))

time1, time2, time3, time4, min_time = 0, 0, 0, 0, 0

# 1. 최대값에 맞춰 전부 쌓기
blocks = b
max_ground = max(grounds)
for g in grounds:
    time1 += max_ground - g
    blocks -= max_ground - g
    if blocks < 0:  # 블럭 모자라면 못 쌓음
        time1 = int(1e9)
        break

# 2. 최소값에 맞춰 전부 깎기
min_ground = min(grounds)
for g in grounds:
    time2 += (g - min_ground) * 2

# 3. 가장 많은 값(같을 시 더 큰 값)에 맞추기
most_ground = Counter(grounds).most_common()
most_ground.sort(key=lambda x: (x[1], x[0]), reverse=True)
most_ground = most_ground[0][0]

for g in grounds:
    # 깎기
    if g > most_ground:
        time3 += (g - most_ground) * 2
    # 쌓기
    elif g < most_ground:
        time3 += most_ground - g
        b -= most_ground - g
        if b < 0:           
            time3 = int(1e9)
            break

# 4. 평균에 맞추기 (blocks 포함)
blocks = b
avg_ground = (sum(grounds) + blocks) // len(grounds)
for g in grounds:
    # 깎기
    if g > avg_ground:
        time4 += (g - avg_ground) * 2
        blocks += g - avg_ground
    # 쌓기
    elif g < avg_ground:
        time4 += avg_ground - g
        blocks -= avg_ground - g
if blocks < 0:
    time4 = int(1e9)


print(time1, time2, time3, time4)
min_time = min(time1, time2, time3, time4)

height = 0
if min_time == time1:
    height = max(height, max_ground)
if min_time == time2:
    height = max(height, min_ground)
if min_time == time3:
    height = max(height, most_ground)
if min_time == time4:
    height = max(height, avg_ground)

print(min_time, height)