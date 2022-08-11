# 11650. 좌표 정렬하기

n = int(input())
pts = []
for _ in range(n):
    a, b = map(int, input().split())
    pts.append([a,b])

pts.sort(key = lambda x: (x[0],x[1]))

for p in pts:
    print(*p)