# 13305. 주유소
# 58점 -> 시간 초과

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

# (리터당 가격, 도시 인덱스)
cities = []
# 마지막 도시는 필요 없음, 리터당 가격 적은 순으로 정렬
for i, price in enumerate(prices[:-1]):
    cities.append([price, i])
cities.sort()

# 리터당 가격 x 도로 길이
total_cost = 0
# 방문한 도로
visited = defaultdict(bool)
# 도로 모두 방문 시 종료하도록
visited_num = n-1

# 리터값 적은 순으로 도로 채우기
for price, city in cities:
    # 현 city 기준 오른쪽에 있고 아직 방문하지 않은 곳만
    for i in range(city, n-1):
        if not visited[i]:
            visited[i] = True
            visited_num -= 1
            total_cost += price * roads[i]
        if visited_num == 0:
                break
        
    if visited_num == 0:
        break

print(total_cost)
