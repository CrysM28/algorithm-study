# 4153. 직각삼각형

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break

    d = max(a, b, c)
    if d != c:
        if d == b:      b, c = c, b
        elif d == a:    a, c = c, a

    if a**2 + b**2 == c**2:     print("right")
    else:   print("wrong")
