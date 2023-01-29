# 18870. 좌표 압축

N = int(input())
points = list(map(int, input().split()))
points_dict = {p: i for i, p in enumerate(sorted(set(points)))}
ans = [points_dict[p] for p in points]
print(*ans)