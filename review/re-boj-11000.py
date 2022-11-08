# 11000. 강의실 배정
## 그리디
import heapq as h

n = int(input())
classes = []
for _ in range(n):
    classes.append(list(map(int, input().split())))
classes.sort(key = lambda x:(x[0], x[1]))


room = []
for start, end in classes:
    # 이거 없어도 어차피 heappush 다음에 room[0] 부르니까 오류 안 남
    if not room:
        h.heappush(room, end)
        continue

    h.heappush(room, end)
    if room[0] <= start:
        h.heappop(room)

print(len(room))
