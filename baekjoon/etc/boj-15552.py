# 빠른 A+B
# 파이썬은 for문으로 대량의 입력을 받을 떄 sys.stdin.readline()
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
