# 3273. 두 수의 합

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

left = 0
right = n - 1
answer = 0
while left < right:
    cur_sum = arr[left] + arr[right]

    if cur_sum == x:
        answer += 1
    elif cur_sum < x:
        left += 1
        continue

    right -= 1

print(answer)