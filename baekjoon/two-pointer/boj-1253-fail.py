# 1253. 좋다
## 음수값 고려를 못함

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

good = 0

for i in range(N-1, 0, -1):
    maybe_good = nums[i]
    left = 0
    right = i-1

    while left <= right:
        cur_sum = nums[left] + nums[right]

        if cur_sum < maybe_good:
            left += 1
        elif cur_sum > maybe_good:
            right += 1
        else:
            print(maybe_good, nums[left], nums[right])
            good += 1
            break

print(good)