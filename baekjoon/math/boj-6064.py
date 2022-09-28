# 6064. 카잉 달력
## 중국인의 나머지 정리

for _ in range(int(input())):
    # <m:n>, <x:y>
    m, n, x, y = map(int, input().split())

    no_answer = True
    while x <= (m * n):
        if x % n == y % n:
            print(x)
            no_answer = False
            break
        x += m
    if no_answer:
        print(-1)