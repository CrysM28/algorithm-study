# 23757. 아이들과 선물 상자
import heapq as h

N, M = map(int, input().split())
presents = list(map(int, input().split()))
children = list(map(int, input().split()))

presents = list(map(lambda x:x*-1, presents))
h.heapify(presents)
happy = True

for child in children:
    present = -h.heappop(presents)

    if present < child:
        happy = False
        break

    present -= child
    if present != 0:
        h.heappush(presents, -present)

if happy:
    print(1)
else:
    print(0)