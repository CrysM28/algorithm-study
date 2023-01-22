# 10942. 팰린드롬?

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[False]*N for _ in range(N)]

for length in range(N):
    for start in range(N-length):
        end = start + length

        # 글자수 1개
        if length == 0:
            dp[start][end] = True
            continue

        # 글자수 2개
        elif length == 1:
            if nums[start] == nums[end]:
                dp[start][end] = True
        
        # 양 끝이 같고 양 끝을 제외한 나머지가 팰린드롬이면 True
        else:
            if nums[start] == nums[end] and dp[start+1][end-1] == True:
                dp[start][end] = True


M = int(input())
for _ in range(M):
    s, e = map(int, input().split())


    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)

