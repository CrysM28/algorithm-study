# for easy problems

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

print(*sorted(nums), sep='\n')