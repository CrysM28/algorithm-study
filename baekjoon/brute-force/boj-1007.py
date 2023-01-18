# 1007. 벡터 매칭
from itertools import combinations
import math

T = int(input())
for _ in range(T):
    result = int(1e9)
    x_total = 0
    y_total = 0

    N = int(input())
    #points = [list(map(int, input().split())) for _ in range(N)]
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        points.append([x,y])

    orders = list(combinations([n for n in range(N)], N//2))
    for order in orders:
        x_plus = x_total
        y_plus = y_total
        x_minus = 0
        y_minus = 0
        for o in order:
            x_plus -= points[o][0]
            x_minus += points[o][0]
            y_plus -= points[o][1]
            y_minus += points[o][1]

        cur_vector = math.sqrt((x_plus - x_minus) ** 2 + (y_plus - y_minus) ** 2)
        result = min(result, cur_vector)


    print(result)


