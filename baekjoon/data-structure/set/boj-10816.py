# 10815 문제와 유사한데 sg_cards에 중복이 있다는 것이 다름

import sys, bisect

n = int(input())
sg_cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
input_cards = list(map(int, sys.stdin.readline().split()))

for c in input_cards:
    lower_bound = bisect.bisect_left(sg_cards, c)
    upper_bound = bisect.bisect_right(sg_cards, c)

    if lower_bound == upper_bound:  # sg_cards에 없는 경우
        print(0, end=" ")
    else:
        print(upper_bound - lower_bound, end=" ")
