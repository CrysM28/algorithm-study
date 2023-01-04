# 2109. 순회강연
import heapq as h

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: x[1])

q = []
for p, d in schedule:
    h.heappush(q, p)
    if len(q) > d:
        h.heappop(q)

print(sum(q))