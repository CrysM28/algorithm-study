# 18870. 좌표 압축
## O(nlogn) + O(n) + O(n) => O(n)

N = int(input())
pts = list(map(int, input().split()))   # 좌표 (points)
pts_sorted = sorted(pts) # 정렬: O(nlogn)
pts_dict = dict()
answer = []
 
# O(n)
idx = 0
for i, p in enumerate(pts_sorted):
    try:
        tmp = pts_dict[p]
    except:
        pts_dict[p] = idx
        idx += 1

# O(n)
for p in pts:
    answer.append(pts_dict[p])

print(*answer, end=" ")