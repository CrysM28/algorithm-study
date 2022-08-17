# 11279. 최대 힙

import heapq as h 
import sys
hp = [] 

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x==0:
        if len(hp) == 0:
        # if not hp:
            print(0)
        else:
            print(h.heappop(hp)[1])
            # print((-1) * h.heappop(hp))
        continue

    h.heappush(hp, (-x,x))
    # h.heappush(hp, -x))