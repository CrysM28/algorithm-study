# 1927. 최소 힙

import heapq as h   # heapq 모듈은 기본적으로 최소 힙 동작
import sys

hp = []     # 힙

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x==0:
        if len(hp) == 0:
            print(0)
        else:
            print(h.heappop(hp))
        continue

    h.heappush(hp, x)