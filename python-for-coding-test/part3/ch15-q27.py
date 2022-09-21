# 정렬된 배열에서 특정 수의 개수 구하기
import bisect

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 이진탐색은 정렬하고 해야함
arr.sort()

left = bisect.bisect_left(arr,x)
right = bisect.bisect_right(arr,x)

num = right-left

if num == 0:
    print(-1)
else:
    print(num+1)