# 회의실 배정

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 먼저 끝나는 것 먼저 배치
meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 0
empty = 0
for start, end in meetings:
    if start >= empty:
        cnt += 1
        empty = end

print(cnt)