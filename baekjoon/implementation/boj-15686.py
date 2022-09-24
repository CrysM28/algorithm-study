# 15686. 치킨 배달
from itertools import combinations

# 도시 크기, 치킨집 최대 개수
n, m = map(int, input().split())

# 전체, 치킨집 위치, 집 위치
graph = []
chickens = []
houses = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 1:
            houses.append((i,j))
        elif t == 2:
            chickens.append((i,j))
    graph.append(tmp)

# print(*graph, sep="\n")
# print(chickens)
# print(houses)




# 선택할 치킨집
chicken_list = list(combinations(chickens, m))
#print(chicken_list)


# 치킨거리 최소값
result = int(1e9)
for c in chicken_list:

    # 치킨집별 도시의 치킨거리
    city_cdist = 0
    for hi, hj in houses:
        # 집별 치킨거리
        h_cdist = int(1e9)
        for ci, cj in c:
            tmp = abs(ci-hi) + abs(cj-hj)
            h_cdist = min(h_cdist, tmp)   # 최소값 갱신

        city_cdist += h_cdist

    result = min(result, city_cdist)
        
print(result)




