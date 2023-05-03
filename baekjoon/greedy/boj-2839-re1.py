# 2839. 설탕 배달

n = int(input())


if n % 5 == 0:
    print(n//5)
else:
    three = 0

    while n > 0:
        n -= 3
        three += 1

        if n % 5 == 0:
            print(n//5 + three)
            break
        elif n == 0:
            print(three)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
