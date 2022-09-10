# 1629. 곱셈
## 분할 정복을 이용한 거듭제곱

def multiply(x, y):
    if y == 1:
        return x % c

    m = multiply(x, y >> 1)  # //2

    if y % 2 == 0:
        return m * m % c
    else:
        return m * m * x % c

a, b, c = map(int, input().split())
result = multiply(a, b)
print(result)




## 시간 초과
# a, b, c = map(int, input().split())
# print((a**b)%c)
