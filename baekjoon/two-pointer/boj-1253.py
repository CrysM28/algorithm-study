# 1253. 좋다

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

good = 0

for i in range(N):
    maybe_good = nums[i]
    left, right = 0, N-1

    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        cur_sum = nums[left] + nums[right]

        if cur_sum < maybe_good:
            left += 1
        elif cur_sum > maybe_good:
            right -= 1
        else:
            #print(left, right, maybe_good)
            good += 1
            break

print(good)