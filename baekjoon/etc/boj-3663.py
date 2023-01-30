# 3663. 고득점

from_A = ord('A') 
from_Z = ord('Z') + 1

for _ in range(int(input())):
    name = input()
    len_name = len(name)
    move = 0

    lr_min = len_name - 1
    for i, n in enumerate(name):
        # 상하
        move += min(ord(n) - from_A, from_Z - ord(n))

        # 좌우
        next_i = i+1
        while next_i < len_name and name[next_i] == 'A':
            next_i += 1
        lr_min = min(lr_min, 2*i + len_name-next_i, i + 2 * (len_name-next_i))

    move += lr_min
    print(move)