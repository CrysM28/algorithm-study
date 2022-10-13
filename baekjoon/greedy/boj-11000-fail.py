# 11000. 강의실 배정
## 시간초과

import sys
input = sys.stdin.readline

n = int(input())
courses = [list(map(int, input().split())) for _ in range(n)]
courses.sort(key=lambda x: (x[1], x[0]))

room = 0

# 강의 전부 배정할 때까지
while courses:
    # 한 강의실에 최대로 배치하기
    room += 1

    last_end = 0
    left = []
    for course in courses:
        start, end = course

        # 배정 성공
        if start >= last_end:
            last_end = end
        # 배정 실패
        else:
            left.append(course)
    courses = left

print(room)