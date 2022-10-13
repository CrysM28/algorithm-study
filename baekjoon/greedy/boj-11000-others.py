import sys
import heapq
input = sys.stdin.readline

answer = 0
n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort(key = lambda x : x[0])

room = []
heapq.heappush(room, lecture[0][1])

for i in range(1, n):
    if lecture[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][1])

    else:
        heapq.heappush(room, lecture[i][1])

print(len(room))

