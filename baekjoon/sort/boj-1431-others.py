# 더 간단하게 가능...

import sys
input = sys.stdin.readline

def condition2(number: str) -> int:
    sumv = 0
    for num in number:
        if num.isnumeric():
            sumv += int(num)

    return sumv

N = int(input())
serial_numbers = []
for _ in range(N):
    serial_numbers.append(input().rstrip())

serial_numbers.sort(key=lambda x: (len(x), condition2(x), x))
print("\n".join(serial_numbers))
