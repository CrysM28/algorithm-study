# 1009. 분산처리

for _ in range(int(input())):
    a, b = map(int, input().split())
    b = (b-1)%4 + 1
    print((a**b-1)%10 + 1)
    