
from itertools import permutations

def solution(k, dungeons):
    max_dun_num = 0

    orders = list(permutations([i for i in range(len(dungeons))]))
    for order in orders:
        cur_hp = k
        cur_dun = 0
        for o in order:
            if cur_hp >= dungeons[o][0]:
                cur_hp -= dungeons[o][1]
                cur_dun += 1
        max_dun_num = max(max_dun_num, cur_dun)

    return max_dun_num



'''
최소 필요 피로도
소모 피로도

최대한 많이 탐험

현재 피로도 k
던전별 최소필요 피로도, 소모피로도 dungeons


'''