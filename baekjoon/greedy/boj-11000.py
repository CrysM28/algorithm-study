# 11000. 강의실 배정
import bisect
import sys

input = sys.stdin.readline

n = int(input())
courses = [list(map(int, input().split())) for _ in range(n)]
courses.sort(key=lambda x: (x[1], x[0]))

# 각 강의실 수업 끝나는 시간 저장
rooms = []

# 수업 하나씩 확인
for course in courses:
    start, end = course

    # 시간표 갱신
    rooms.append(end)

    # 기존 강의실 재활용 -> 현 수업 시작시간이 강의실 가장 먼저 끝나는 시간보다 늦으면 됨
    right_idx = bisect.bisect_right(rooms, start)
    if right_idx != 0:
        left_idx = bisect.bisect_left(rooms, start)
        if left_idx == right_idx:
            left_idx -= 1
        rooms.pop(left_idx)

print(len(rooms))
