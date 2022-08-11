# 2805. 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

lo, hi = 0, max(trees)

while lo <= hi:
    height = (lo + hi) // 2
    total = 0

    for t in trees:
        if t > height:
            total += t - height

    # 더 높게 자르자
    if total >= m:
        lo = height + 1

    # 더 짧게 자르자
    elif total < m:
        hi = height - 1

# 최대값이므로 hi 출력
print(hi)
