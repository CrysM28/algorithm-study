# 근데 이거보다 내 풀이가 더 적게 걸림
# 피로도.py -> 최대 50~60ms
# 이거 -> 최대 140ms
    # 매번 max 해주는거 cost가 더 큰 거 같음

from itertools import permutations


def solution(k, dungeons):
    max_cnt = 0
    N = len(dungeons)

    # 순열을 더 간단히 나타낼 수 있음
    for perm in permutations(range(N)):
        curr_k = k
        cnt = 0

        for p in perm:
            if curr_k >= dungeons[p][0]:
                curr_k -= dungeons[p][1]
                cnt += 1
                # 늘어날때마다 매번 갱신하기
                max_cnt = max(max_cnt, cnt)
            # 아닐 경우 순열 중지해서 효율성 올리기
            else:
                break

    return max_cnt


"""
- permutations
"""