# 1781. 컵라면
import heapq as h

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]
problems.sort()

q = []
for time, cup in problems:
    h.heappush(q, cup)
    if time < len(q):
        h.heappop(q)

print(sum(q))
    
