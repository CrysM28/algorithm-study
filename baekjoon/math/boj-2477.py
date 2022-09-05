# 2477: 참외밭

melon = int(input())  # 제곱미터 당 참외의 수
p = 6  # 참외밭 둘레 개수

# 참외밭
farm = []
for i in range(p):
    pos, length = map(int, input().split())
    farm.append([pos, length])

# 큰 사각형
max_x, max_y = 0, 0
for f in farm:
    if f[0] == 1 or f[0] == 2:
        max_y = max(max_y, f[1])
    if f[0] == 3 or f[0] == 4:
        max_x = max(max_x, f[1])

# 작은 사각형
found = False
i = 0

## 연속되는 두 방향 중 가운데 두 개가 작은 사각형의 변
while not found:
    repeat1 = farm[i % p]
    repeat2 = farm[(i + 1) % p]
    if repeat1[0] == farm[(i + 2) % p][0] and repeat2[0] == farm[(i + 3) %
                                                                 p][0]:
        found = True
        repeat1 = farm[(i + 1) % p]
        repeat2 = farm[(i + 2) % p]
    i += 1

if repeat1[0] == 1 or repeat1[0] == 2:
    min_x = repeat2[1]
    min_y = repeat1[1]
else:
    min_x = repeat1[1]
    min_y = repeat2[1]


# 결과
area = (max_x * max_y) - (min_x * min_y)
print(area * melon)
