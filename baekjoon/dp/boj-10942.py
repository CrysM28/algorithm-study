# 10942. 팰린드롬?
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    s, e = map(int, input().split())

    tmp = nums[s-1:e]

    if tmp == tmp[::-1]:
        print(1)
    else:
        print(0)

