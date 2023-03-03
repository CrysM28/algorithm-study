# 1934. 최소공배수

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

def lcm(x, y):
    return (x*y) // gcd(x,y)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))