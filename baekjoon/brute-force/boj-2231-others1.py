# 다른 풀이 1

n = int(input())
for i in range(n):
    a = sum(map(int, str(i + 1))) + int(i + 1)
    if a == n:
        print(i + 1)
        break
    if i + 1 == n:
        print(0)


d = map(int, "21")
print(*d)