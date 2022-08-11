# 10989. 수 정렬하기 3
## 시간 제한은 널널한 대신(5초) 메모리 제한이 빡센 문제(8MB)

import sys
input= sys.stdin.readline

n = int(input())
ints = [0] * 10001

for _ in range(n):
    ints[int(input())] += 1

for i in range(1, 10001):
    while ints[i] > 0:
        print(i)
        ints[i] -= 1
