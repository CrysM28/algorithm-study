# 10773. 제로

k = int(input())
total = []

for _ in range(k):
    num = int(input())

    if num == 0:
        total.pop()
    else:
        total.append(num)

print(sum(total))