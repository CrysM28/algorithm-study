# 1931. 회의실 배정
## 그리디

n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort(key=lambda x: (x[1], x[0]))

meetings = 0
last_end = 0

for t in timetable:
    start, end = t
    if start >= last_end:
        last_end = end
        meetings += 1

print(meetings)