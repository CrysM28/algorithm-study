# 9205. 맥주 마시면서 걸어가기
from collections import deque

# 좌표 거리 구하기
def get_dist(pos1, pos2):
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    return x + y

# 맥주 20개로 갈 수 있는 거리인지 (50m당 1병 -> 최대 1000m)
def is_beer_enough(pos1, pos2):
    dist = get_dist(pos1, pos2)
    if dist <= 1000:
        return True
    else: return False


for _ in range(int(input())):
    # 맥주 편의점 수
    n = int(input())

    # 좌표
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))

    # BFS
    visited = {home}
    queue = deque([home])
    is_happy = False

    while queue:
        cur = queue.popleft()

        if is_beer_enough(cur, festival):
            is_happy = True
            break

        for next in stores:
            if next not in visited:
                if is_beer_enough(cur, next):
                    visited.add(next)
                    queue.append(next)

    # 결과
    if is_happy:
        print("happy")
    else:
        print("sad")
