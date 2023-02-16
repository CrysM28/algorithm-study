# 17298. 오큰수

n = int(input())
nums = list(map(int, input().split()))

ans = [-1] * n
big = [nums[-1]]

for i in range(n-2, -1, -1):
    if nums[i] < big[-1]:
        ans[i] = big[-1]
        big.append(nums[i])
    else:
        while big and nums[i] >= big[-1]:
            big.pop()
        if big:
            ans[i] = big[-1]
        big.append(nums[i])


print(*ans)