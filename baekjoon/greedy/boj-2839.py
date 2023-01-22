# 2839. 설탕 배달

n = int(input())
max_try = n // 3 + 1
bag = 0

for i in range(max_try):
    for j in range(max_try):
        if 5*i + 3*j == n:
            bag = i + j
            break

if bag == 0:
    print(-1)
else:
    print(bag)