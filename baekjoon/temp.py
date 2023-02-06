
N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(nums)
ans = 0

for i in range(1, N+1):
    for n in nums:
        if i%n == 0:
            ans += i
            break

print(ans)