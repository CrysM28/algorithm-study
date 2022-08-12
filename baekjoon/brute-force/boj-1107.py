# 1107. 리모컨

import bisect

cur_ch = 100
target_ch = int(input())
broken_button_num = int(input())
broken = set(map(int, input().split()))
alive = list(set([x for x in range(10)]) - broken)


digit = len(str(target_ch))     # 타겟 채널 자리수
close_ch = 0

for d in range(1, digit+1):
    cur_digit = (target_ch % 10**d) // 10**(d-1)

    if cur_digit in alive:
        print("yes")
    #print(cur_digit)




