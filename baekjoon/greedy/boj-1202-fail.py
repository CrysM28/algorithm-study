# 1202. 보석 도둑
## 시간초과
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# (무게, 가격)
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 보석: 가격 내림차순, 무게 오름차순
jewels.sort(key=lambda x: (-x[1], x[0]))
# 가방: 무게 오름차순
bags.sort()

total = 0
for jewel in jewels:
    # print("jewel", jewel)
    # print("bag left", bags)
    weight, cost = jewel

    # 가방 다 썼으면 끝
    if not bags:
        break

    # 현재 무게 넣을 수 있는 가방 없으면 스킵
    if weight > bags[-1]:
        continue

    # 넣을 수 있는 최소무게 가방 찾기
    tmp_bags = []
    for i in range(len(bags)):
        if weight <= bags[i]:
            total += cost
            bags = tmp_bags + bags[i+1:]
            break
        tmp_bags.append(bags[i])


print(total)