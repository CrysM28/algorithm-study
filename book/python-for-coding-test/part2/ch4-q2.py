# 왕실의 나이트

from itertools import product

a = input()
row = int(a[1])
col = int(ord(a[0]) - ord('a')) + 1

# 이동 가능한 횟수
count = 0

# 가능한 움직임
moves = list(product((1, -1), (2, -2)))

for m in moves:
    # 1: UD 1칸, LR 2칸
    r = row + m[0]
    c = col + m[1]
    if r >= 1 and c >= 1 and r <= 8 and c <= 8:
        count += 1

    # 2: UD 2칸, LR 1칸
    r = row + m[1]
    c = col + m[0]
    if r >= 1 and c >= 1 and r <= 8 and c <= 8:
        count += 1


print(count)