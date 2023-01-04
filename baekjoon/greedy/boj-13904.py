# 13094. 과제
import heapq as h

N = int(input())

assignments = [list(map(int, input().split())) for _ in range(N)]
# assignments = []
# for _ in range(N):
#     d, w = map(int, input().split())
#     assignments.append((d, w))
assignments.sort()

queue = []
for assignment in assignments:
    d, w = assignment
    h.heappush(queue, w)
    if len(queue) > d:
        h.heappop(queue)

#print(queue)
print(sum(queue))