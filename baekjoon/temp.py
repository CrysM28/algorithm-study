
for _ in range(int(input())):
    a, b = map(int, input().split())
    res = a**b
    print(res%10)