# 1202. 보석 도둑
import heapq as h
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# (무게, 가격)
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 무게순 정렬
jewels.sort()
bags.sort()

# 가방에 들어갈 수 있는 후보 보석
candidates = []
total = 0

for bag in bags:
    # 가방에 넣을 수 있는 무게면 가격 높은 순으로
    while jewels and jewels[0][0] <= bag:
        weight, cost = h.heappop(jewels)
        h.heappush(candidates, -cost)

    # 후보 중에 가장 가격이 높은 것 하나 넣기
    if candidates:
        total += -h.heappop(candidates)

print(total)