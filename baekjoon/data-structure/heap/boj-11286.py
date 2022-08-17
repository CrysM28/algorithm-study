# 11286. 절댓값 힙

import heapq as h
import sys

hp = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x == 0:
        if hp:
            print(h.heappop(hp)[1])
        else:
            print(0)

    else:
        h.heappush(hp, (abs(x), x))
