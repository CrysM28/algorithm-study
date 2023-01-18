# 10942. 팰린드롬?
## 이게 dp문제일거라곤 생각도 안해봄

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

