x = int(input())
n = 1
idx = 0


def sum_to_num(num):
    return (1 + num) * num // 2


# 위치(인덱스) 찾기
while True:
    if x <= sum_to_num(n):
        idx = x - sum_to_num(n - 1)
        break
    else:
        n += 1

# 분수 숫자
i, j = 0, 0
if n % 2 == 0:
    i = idx
    j = n - idx + 1
else:
    i = n - idx + 1
    j = idx

print('{}/{}'.format(i, j))