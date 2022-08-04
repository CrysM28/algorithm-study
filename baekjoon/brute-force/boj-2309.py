# 일곱 난쟁이
## brute-force

import sys
from itertools import combinations

dwarfs = []
for i in range(9):
    dwarfs.append(int(sys.stdin.readline()))

# 모든 조합을 찾고 합 구하기
dwarf_comb = list(combinations(dwarfs, 7))

for d7_list in dwarf_comb:
    total_height = 0
    for d in d7_list:
        total_height += d
    #print(d7_list, total_height)
    if total_height == 100:
        for i in sorted(list(d7_list)):
            print(i)
        break   
