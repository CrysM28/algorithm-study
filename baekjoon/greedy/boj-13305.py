# 13305. 주유소
import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

total_cost = 0
min_cost = cities[0]

for i in range(n-1):
    # 더 작은 기름값 나오면 그 때 변경
    if min_cost > cities[i]:
        min_cost = cities[i]
    total_cost += min_cost * roads[i]

print(total_cost)
