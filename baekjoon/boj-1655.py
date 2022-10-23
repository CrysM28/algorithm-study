# 1655. 가운데를 말해요
import heapq
import sys
input = sys.stdin.readline

n = int(input())

left_heap = []
right_heap = []
answer = []

for i in range(n):
    number = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -number)
    else:
        heapq.heappush(right_heap, number)

    if right_heap and -left_heap[0] > right_heap[0]:
        big = heapq.heappop(left_heap)
        small = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -small)
        heapq.heappush(right_heap, -big)

    answer.append(-left_heap[0])

print(*answer, sep='\n')