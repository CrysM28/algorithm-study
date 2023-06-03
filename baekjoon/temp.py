
T = int(input())

a, b, c = 0, 0, 0

ta, tb, tc = 300, 60, 10

if T > ta:
    a = T // ta
    T %= ta
if T > tb:
    b = T // tb
    T %= tb
if T > tc:
    c = T // tc
    T %= tc

if T != 0:
    print(-1)
else:
    print(a, b, c)
