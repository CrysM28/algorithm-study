# 2110. 공유기 설치

n, c = map(int, input().split())
routers = sorted([int(input()) for _ in range(n)])

lo, hi = 1, routers[-1] - routers[0]

while lo <= hi:
    distance = (lo + hi) // 2
    count = 1
    cur_router = routers[0]

    # 결정함수: 주어진 dis로 꽂을 수 있는 최대 공유기 수
    for i in range(1, n):
        if cur_router + distance <= routers[i]:
            count += 1
            cur_router = routers[i]

    # 더 넓게 배치해보자
    if count >= c:
        lo = distance + 1

    # 더 좁게 배치해보자
    elif count < c:
        hi = distance - 1

print(hi)