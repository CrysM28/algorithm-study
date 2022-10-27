# 25629. 홀짝 수열

n = int(input())
numbers = list(map(int, input().split()))
#numbers.sort()

# 홀짝 나누기
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

# 길이 조건만 맞추면 됨
if len(odd) == len(even) or len(odd) == len(even) + 1:
    print(1)
else:
    print(0)


# print(odd)
# print(even)
# print(possible)
