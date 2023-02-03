# 2470. 두 용액

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n-1
sol1, sol2 = 0, 0
min_val = int(1e10)


while left < right:
    mix = arr[left] + arr[right]

    if min_val > abs(mix):
        min_val = abs(mix)
        sol1 = arr[left]
        sol2 = arr[right]
    
    if mix == 0:
        break

    if mix < 0:
        left += 1
    else:
        right -= 1

if sol1 < sol2:
    print(sol1, sol2)
else:
    print(sol2, sol1)