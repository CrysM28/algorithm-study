# 11000. 강의실 배정
import sys
import heapq as h

input = sys.stdin.readline

n = int(input())
courses = [list(map(int, input().split())) for _ in range(n)]
courses.sort()

# 각 강의실 수업 끝나는 시간 저장
rooms = []

# 수업 하나씩 확인
for course in courses:
    start, end = course

    # 시간표 갱신
    h.heappush(rooms, end)

    # 기존 강의실 재활용 가능하면 
    if start >= rooms[0]:
        h.heappop(rooms)

print(len(rooms))
