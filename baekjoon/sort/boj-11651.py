# 11650. 좌표 정렬하기 2
## x,y 정렬순서 조건만 바뀜

n = int(input())
pts = []
for _ in range(n):
    a, b = map(int, input().split())
    pts.append([a,b])

pts.sort(key = lambda x: (x[1],x[0]))

for p in pts:
    print(*p)