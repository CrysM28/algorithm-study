# 네 번째 점
# 중복 아닌 숫자만 골라내면 됨

from collections import Counter

x,y = [], []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x_count = dict(Counter(x))
y_count = dict(Counter(y))

for key, value in x_count.items():
    if value == 1:
        my_x = key
for key, value in y_count.items():
    if value == 1:
        my_y = key

print(my_x, my_y)