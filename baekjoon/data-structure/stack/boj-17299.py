# 17299. 오등큰수

n = int(input())
nums = list(map(int, input().split()))

ans = [-1] * n
stack = [nums[0]]
