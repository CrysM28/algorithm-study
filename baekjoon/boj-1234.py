# 1234. 크리스마스 트리
import sys
from math import factorial
sys.setrecursionlimit(10**6)

def find(i, r, g, b, count):
    global total
    global end

    if i > N:
        end = True
        total += count
        return

    # 같은 색
    if r-i >= 0:
        find(i+1, r-i, g, b, count)
    if g-i >= 0:
        find(i+1, r, g-i, b, count)
    if b-i >= 0:
        find(i+1, r, g, b-i, count)

    # i//2
    i2 = i // 2
    if i % 2 == 0:
        tmp = factorial(i) // factorial(i2)**2
        if r-i2 >= 0 and g-i2 >= 0:
            find(i+1, r-i2, g-i2, b, count*tmp)
        if r-i2 >= 0 and b-i2 >= 0:
            find(i+1, r-i2, g, b-i2, count*tmp)
        if g-i2 >= 0 and b-i2 >= 0:
            find(i+1, r, g-i2, b-i2, count*tmp)

    # i//3
    i3 = i // 3
    if i % 3 == 0 and r-i3 >= 0 and g-i3 >= 0 and b-i3 >= 0:
        tmp = factorial(i) // factorial(i3)**3
        find(i+1, r-i3, g-i3, b-i3, count*tmp)
        


N, R, G, B = map(int, input().split())

end = False
total = 0

find(1, R, G, B, 1)

if end:
    print(total)
else:
    print(0)