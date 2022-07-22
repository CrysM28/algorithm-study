## 아직 다 안 푼 문제 - 보류

import sys

dwarf_9 = []
dwarf_7 = []
total_height = 0

# input
for i in range(9):
    dwarf_9.append(int(sys.stdin.readline()))


for i in range(9):
    idx = 0

    for j in range(i, 9):
        if idx == i or idx == j:
            print(idx)
        
        idx += 1


# while total_height != 100:
#     skip1 = i
#     skip2 = 8-i

#     for d in dwarf_9:
#         if 
#         total_height += d
#         dwarf_7.append(d)
#         if total_height == 100:
#             print(dwarf_7.sort())
#             break
#         elif total_height > 100:
#             total_height = 0