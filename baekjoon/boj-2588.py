# 곱셈

a = input()
b = input()
b_reverse = b[::-1]

for b_digit in b_reverse:
    print(int(a) * int(b_digit))

print(int(a) * int(b))
