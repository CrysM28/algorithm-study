import math
a, b = map(int, input().split())

# 최대공약수 (GCD)
## 브루트 포스
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

## 유클리드 호제법
### x % y = r 일 때, GCD(x,y) = GCD(y,r)
def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x

## math 모듈
math.gcd(a, b)


# 최소공배수 (LCM)
## 브루트 포스
for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

## 유클리드 호제법
def LCM(x, y):
    return (x * y) // GCD(x, y)

## math 모듈 (3.9 이상)
math.lcm(a, b)

